<script>
    import { Circle } from 'svelte-loading-spinners'

    export let label="Click Me"
    export let secondaryButton = false;
    export let loading;
    export let disabled;
</script>

<button on:click {...$$restProps} class="{secondaryButton ? "secondary-button" : ""} {disabled || loading ? "disabled" : ""}" disabled={disabled || loading}>
    {#if loading}
    <span class="loader-span">
        <Circle color="#E7E4FA" size="30"/>
    </span>
    {:else}
        {label}
    {/if}
</button>

<style>
    button {
        background-color: var(--purple-2);
        color: var(--white);
        width: 100%;
        height: 51px;
        font: var(--primary-font-semibold);
        border-radius: 5px;
        border: none;
        outline:none;
        cursor: pointer;
        margin-bottom: 15px;
    }
    .secondary-button {
        background-color: var(--white);
        color: var(--purple-2);
        border: 2px var(--purple-2) solid;
    }
    .loader-span {
        display: flex;
        width: 100%;
        justify-content: center;
    }
    .disabled {
        cursor: auto;
    }
</style>