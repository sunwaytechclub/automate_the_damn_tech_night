<script>
    export let type = "text";
    export let placeholder = "Username";
    export let label = "Username";
    export let disabled = false;
    export let error = {
        enabled: false,
        message: "Invalid"
    }
    export let instance = undefined;
</script>

<div>
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>{label}</label>

    <input class="{disabled ? "disabled" : ""} {error.enabled ? "error" : ""}" {type} {placeholder} {disabled} {...$$restProps} bind:this={instance}/>
    {#if error.enabled}
        <p class="error-message">{error.message}</p>
    {/if}
</div>

<style>
    label {
        font-weight: 600;
        margin-bottom: 10px;
        display: block;
        color: var(--dark-blue);
    }

    input {
        background-color: var(--light-grey);
        border: none;
        height: 51px;
        padding: 0 20px;
        outline: none;
        font-family: var(--primary-font);
        font-weight: 500;
        font-size: 14px;
        width: 100%;
        border-radius: 5px;
        margin-bottom: 15px;
    }
    .disabled {
        color: var(--medium-grey)
    }
    .error {
        border: 2px var(--red) solid;
    }
    .error-message {
        font: var(--primary-font-regular);
        font-size: 12px;
        color: var(--red);
        margin-bottom: 15px;
        margin-top: -10px;
    }
    ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
        color: var(--dark-grey);
        opacity: 1; /* Firefox */
    }

        :-ms-input-placeholder { /* Internet Explorer 10-11 */
        color: var(--dark-grey);
    }

        ::-ms-input-placeholder { /* Microsoft Edge */
        color: var(--dark-grey);
    }
</style>