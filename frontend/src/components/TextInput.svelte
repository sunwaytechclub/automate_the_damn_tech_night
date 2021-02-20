<script>
    export let type = "text";
    export let placeholder = "Username";
    export let label = "Username";
    export let value;
    export let disabled;
</script>

<!-- svelte-ignore a11y-label-has-associated-control -->
<label>{label}</label>

<input class="{disabled ? "disabled" : ""}"{type} {placeholder} {disabled} {...$$restProps} bind:this={value}/>

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
</style>