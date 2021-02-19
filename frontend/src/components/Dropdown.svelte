<script>
    import Select from 'svelte-select';

    export let items = [
        {value: 'chocolate', label: 'Chocolate'},
        {value: 'pizza', label: 'Pizza'},
        {value: 'cake', label: 'Cake'},
        {value: 'chips', label: 'Chips'},
        {value: 'ice-cream', label: 'Ice Cream'},
        ];

    export let selectedValue
    export let placeholder = "Speaker name"

    function handleSelect(event) {
    console.log('selected item=', event.detail);
    // .. do something here 🙂
    }
</script>

<div class="themed">
<Select {items} {selectedValue} {placeholder} on:select={handleSelect}></Select>
</div>

<style>
.themed {
    --borderRadius: 5px;
    --background: var(--light-grey);
    --itemIsActiveBG: var(--purple-2);
    --itemHoverBG: var(--light-purple-2);
    --border: none;
    --height: 51px;
    font: var(--primary-font-medium);
    margin-bottom: 15px;
  }
</style>