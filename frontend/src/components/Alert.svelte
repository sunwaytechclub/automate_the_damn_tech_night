<script>
    import { fly } from 'svelte/transition';
	import { quintInOut } from 'svelte/easing';

    export let alertText = "Alert"
    export let visible = false;
</script>

{#if visible}
    <div class="wrapper">
        <div class="container" transition:fly="{{duration: 700, y: -100, opacity: 0.5, easing: quintInOut}}">
            <p class="alert-text">{alertText}</p>
            <img src="/assets/icons/close-small-red.svg" alt="close" class="close-icon" on:click={() => {visible = false}}/>
        </div>
    </div>
{/if}

<style>
    .wrapper {
        width: 100vw;
        display: flex;
        justify-content: center;
        position: fixed;
        top: 30px;
        z-index: 6;
    }
    .container {
        padding: 10px 30px;
        background-color: var(--light-red);
        color: var(--red);
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .close-icon {
        margin-left: 10px;
        margin-right: -10px;
        cursor: pointer;
    }
    @media only screen and (max-width: 966px) {
        .wrapper {
            top: 60px
        }
    }
</style>