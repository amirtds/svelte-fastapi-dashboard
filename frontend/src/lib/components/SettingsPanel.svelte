<script lang="ts">
  import { fade } from 'svelte/transition';
  
  export let tempThreshold = 25;
  export let humidityThreshold = 60;
  let isOpen = false;
  
  function updateSettings() {
    // Save the settings
    tempThreshold = tempThreshold;
    humidityThreshold = humidityThreshold;
    // Close the panel
    isOpen = false;
  }
</script>

<div class="settings-container">
  <button class="settings-button" on:click={() => isOpen = !isOpen}>
    ⚙️ Settings
  </button>
  
  {#if isOpen}
    <div class="settings-panel" transition:fade>
      <h3>Alert Thresholds</h3>
      <div class="setting-group">
        <label>
          Temperature (°C)
          <input type="number" bind:value={tempThreshold} min="0" max="40" step="0.5">
        </label>
      </div>
      <div class="setting-group">
        <label>
          Humidity (%)
          <input type="number" bind:value={humidityThreshold} min="0" max="100" step="5">
        </label>
      </div>
      <div class="button-group">
        <button class="cancel" on:click={() => isOpen = false}>Cancel</button>
        <button class="save" on:click={updateSettings}>Save</button>
      </div>
    </div>
  {/if}
</div>

<style>
  .settings-container {
    position: fixed;
    bottom: 1rem;
    right: 1rem;
    z-index: 1000;
  }
  
  .settings-button {
    background: #2c3e50;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .settings-button:hover {
    background: #34495e;
  }
  
  .settings-panel {
    position: absolute;
    bottom: 100%;
    right: 0;
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    margin-bottom: 0.5rem;
    min-width: 280px;
    color: #2c3e50;
  }
  
  h3 {
    margin: 0 0 1rem 0;
    font-size: 1.2rem;
    color: #2c3e50;
  }
  
  .setting-group {
    margin: 1rem 0;
  }
  
  label {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    font-size: 0.9rem;
    color: #34495e;
  }
  
  input {
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
    width: 100%;
  }
  
  input:focus {
    outline: none;
    border-color: #3498db;
    box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
  }
  
  .button-group {
    display: flex;
    justify-content: flex-end;
    gap: 0.5rem;
    margin-top: 1.5rem;
  }
  
  .button-group button {
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9rem;
    transition: opacity 0.2s;
  }
  
  .button-group button:hover {
    opacity: 0.9;
  }
  
  .save {
    background: #2ecc71;
    color: white;
  }
  
  .cancel {
    background: #95a5a6;
    color: white;
  }
</style>