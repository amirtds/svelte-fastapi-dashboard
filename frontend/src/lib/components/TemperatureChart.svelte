<script lang="ts">
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';
  import type { SensorReading } from '$lib/types';

  export let data: SensorReading[];
  let canvas: HTMLCanvasElement;
  let chart: Chart;

  $: if (chart && data) {
    chart.data.labels = data.map(reading => {
      const date = new Date(reading.timestamp);
      return date.toLocaleTimeString();
    });
    chart.data.datasets[0].data = data.map(reading => reading.temperature);
    chart.update();
  }

  onMount(() => {
    chart = new Chart(canvas, {
      type: 'line',
      data: {
        labels: [],
        datasets: [{
          label: 'Temperature (°C)',
          data: [],
          borderColor: '#3498db',
          tension: 0.4,
          fill: false
        }]
      },
      options: {
        responsive: true,
        animation: {
          duration: 0 // Disable animations for real-time updates
        },
        scales: {
          y: {
            beginAtZero: false,
            suggestedMin: 15,
            suggestedMax: 30
          }
        }
      }
    });

    return () => {
      chart.destroy();
    };
  });
</script>

<canvas bind:this={canvas}></canvas>