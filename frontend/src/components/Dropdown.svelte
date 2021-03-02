<script>
    import Select from 'svelte-select';

    export let items = [
        {value: 'chocolate', label: 'Chocolate'},
        {value: 'pizza', label: 'Pizza'},
        {value: 'cake', label: 'Cake'},
        {value: 'chips', label: 'Chips'},
        {value: 'ice-cream', label: 'Ice Cream'},
        ];

    export let selectedValue = ""
    export let placeholder = "Speaker name"
    export let label;
    export let disabled = false;

</script>

<div class="themed {disabled ? "disabled" : ""}">
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>{label}</label>
    <Select {items} {selectedValue} {placeholder} on:select isDisabled={disabled}></Select>
</div>

<style>
    label {
        font-weight: 600;
        margin-bottom: 10px;
        display: block;
        color: var(--dark-blue);
    }
    .disabled {
        color: var(--medium-grey)
    }
    
    .themed {
        --borderRadius: 5px;
        --background: var(--light-grey);
        --itemIsActiveBG: var(--purple-2);
        --itemHoverBG: var(--light-purple-2);
        --placeholderColor: var(--dark-grey);
        --border: none;
        --height: 51px;
        font: var(--primary-font-medium);
        margin-bottom: 15px;
    }
</style>