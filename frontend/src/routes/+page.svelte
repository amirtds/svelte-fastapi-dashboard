<script lang="ts">
  import { onMount } from 'svelte';
  import TemperatureChart from '$lib/components/TemperatureChart.svelte';
  import HumidityGauge from '$lib/components/HumidityGauge.svelte';
  import SettingsPanel from '$lib/components/SettingsPanel.svelte';
  import AlertBanner from '$lib/components/AlertBanner.svelte';
  import type { SensorReading } from '$lib/types';

  let currentReading = $state<SensorReading | null>(null);
  let historicalData = $state<SensorReading[]>([]);
  let eventSource = $state<EventSource | undefined>(undefined);
  let tempThreshold = $state(25);
  let humidityThreshold = $state(60);
  let alertMessage = $state('');
  let alertType = $state<'warning' | 'critical'>('warning');

  function checkAlertConditions(reading: SensorReading) {
    if (reading.temperature > tempThreshold) {
      alertMessage = `High temperature detected: ${reading.temperature}°C`;
      alertType = 'critical';
    } else if (reading.humidity > humidityThreshold) {
      alertMessage = `High humidity detected: ${reading.humidity}%`;
      alertType = 'warning';
    } else {
      alertMessage = '';
    }
  }

  // Reactive effect to check alerts when thresholds or readings change
  $effect(() => {
    if (currentReading) {
      checkAlertConditions(currentReading);
    }
  });

  onMount(async () => {
    // Initial data fetch
    const response = await fetch('http://localhost:8000/current');
    currentReading = await response.json();
    historicalData = [currentReading];

    // Set up SSE connection
    eventSource = new EventSource('http://localhost:8000/stream');
    eventSource.addEventListener('sensor_update', (event) => {
      currentReading = JSON.parse(event.data);
      historicalData = [...historicalData, currentReading].slice(-30); // Keep last 30 readings
      if (currentReading) {
        checkAlertConditions(currentReading);
      }
    });

    return () => {
      if (eventSource) eventSource.close();
    };
  });
</script>

<AlertBanner message={alertMessage} type={alertType} />

<main class="container">
  <h1>Sensor Dashboard</h1>

  {#if currentReading}
    <div class="dashboard-grid">
      <div class="card span-2">
        <h2>Temperature History</h2>
        <TemperatureChart data={historicalData} />
      </div>

      <div class="card">
        <h2>Current Humidity</h2>
        <HumidityGauge value={currentReading.humidity} />
      </div>

      <div class="card">
        <h2>System Status</h2>
        <div class="status-container">
          <div class="status-indicator {currentReading.status}"></div>
          <p class="status-text">{currentReading.status}</p>
          <p class="timestamp">Last updated: {new Date(currentReading.timestamp).toLocaleTimeString()}</p>
        </div>
      </div>
    </div>
  {/if}
</main>

<style>
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 2rem;
  }

  .card {
    background: #fff;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  .span-2 {
    grid-column: span 2;
  }

  .status-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .status-indicator {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin: 1rem 0;
  }

  .status-indicator.normal { background-color: #2ecc71; }
  .status-indicator.warning { background-color: #f1c40f; }
  .status-indicator.critical { background-color: #e74c3c; }

  .status-text {
    text-transform: uppercase;
    font-weight: bold;
  }

  .timestamp {
    color: #666;
    font-size: 0.9rem;
  }

  @media (max-width: 768px) {
    .dashboard-grid {
      grid-template-columns: 1fr;
    }

    .span-2 {
      grid-column: auto;
    }
  }
</style>

<SettingsPanel 
  tempThreshold={tempThreshold} 
  humidityThreshold={humidityThreshold} 
  onTempChange={(value) => tempThreshold = value}
  onHumidityChange={(value) => humidityThreshold = value}  
/>