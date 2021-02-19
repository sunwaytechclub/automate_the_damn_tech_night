<script>
    export let label="Click Me"
    export let secondaryButton = false;
</script>

<button on:click {...$$restProps} class="{secondaryButton ? "secondary-button" : ""}">{label}</button>

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
</style>