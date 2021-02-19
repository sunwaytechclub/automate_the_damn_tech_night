<script>
    import Flatpickr from 'svelte-flatpickr'

    import 'flatpickr/dist/flatpickr.css'
    import 'flatpickr/dist/themes/light.css'

    export let time = null
    const flatpickrOptions = {
        element: '#my-time-picker',
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
    }
    
</script>

<Flatpickr options="{ flatpickrOptions }" bind:value={time} element="#my-time-picker">
    <div class="flatpickr" id="my-time-picker">
        <input type="text" placeholder="Select Time.." data-input>
        
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
        padding: 0 15px;
    }
    .flatpickr {
        margin-bottom: 15px;
    }
</style>