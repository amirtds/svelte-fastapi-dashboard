<script lang="ts">
  import { fade } from 'svelte/transition';

  const { message, type = 'warning' } = $props<{ 
    message: string; 
    type?: 'warning' | 'critical'
  }>();
</script>

{#if message}
  <div class="alert {type}" transition:fade>
    <span class="alert-icon">⚠️</span>
    {message}
  </div>
{/if}

<style>
  .alert {
    position: fixed;
    top: 1rem;
    right: 1rem;
    padding: 1rem;
    border-radius: 4px;
    color: white;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    z-index: 1000;
  }

  .warning {
    background-color: #f1c40f;
  }

  .critical {
    background-color: #e74c3c;
  }

  .alert-icon {
    font-size: 1.2rem;
  }
</style>