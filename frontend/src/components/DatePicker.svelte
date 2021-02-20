<script>
    import Flatpickr from 'svelte-flatpickr'

    import 'flatpickr/dist/flatpickr.css'
    import 'flatpickr/dist/themes/light.css'

    export let date = null
    const flatpickrOptions = {
        element: '#my-date-picker'
    }
    
</script>

<Flatpickr options="{ flatpickrOptions }" bind:value={date} element="#my-date-picker">
    <div class="flatpickr" id="my-date-picker">
        <input type="text" placeholder="Select Date.." data-input>

        <!-- svelte-ignore a11y-missing-attribute -->
        <a class="input-button" title="clear" data-clear>
                <i class="icon-close"></i>
        </a>
    </div>
</Flatpickr>

<style>
    input {
        height: 51px;
        width: 100%;
        border-radius: 5px;
        outline: none;
        background-color: var(--light-grey);
        border: none;
        padding: 0 20px;
    }
    .flatpickr {
        margin-bottom: 15px;
    }
</style>