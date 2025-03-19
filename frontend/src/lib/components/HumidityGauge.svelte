<script lang="ts">
  import { onMount } from 'svelte';
  import Chart from 'chart.js/auto';

  export let value: number;
  let canvas: HTMLCanvasElement;
  let chart: Chart;

  $: if (chart && value !== undefined) {
    chart.data.datasets[0].data = [value];
    chart.update();
  }

  onMount(() => {
    chart = new Chart(canvas, {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [value],
          backgroundColor: ['#2ecc71'],
          circumference: 180,
          rotation: 270,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          tooltip: {
            enabled: false
          }
        }
      }
    });

    return () => {
      chart.destroy();
    };
  });
</script>

<div class="gauge-container">
  <canvas bind:this={canvas}></canvas>
  <div class="gauge-value">{value}%</div>
</div>

<style>
  .gauge-container {
    position: relative;
    height: 200px;
  }

  .gauge-value {
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    font-size: 1.5rem;
    font-weight: bold;
  }
</style>