<script>
    import Flatpickr from 'svelte-flatpickr'

    import 'flatpickr/dist/flatpickr.css'
    import 'flatpickr/dist/themes/light.css'

    export let date = null
    export let label = "Date"
    export let error = {
        enabled: false,
        message: "Invalid"
    }
    
    const flatpickrOptions = {
        element: '#my-date-picker'
    }
    
</script>
<div>
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>{label}</label>

    <Flatpickr options="{ flatpickrOptions }" bind:value={date} element="#my-date-picker">
        <div class="flatpickr" id="my-date-picker">
            <input type="text" placeholder="Select Date.." data-input class="{error.enabled ? "error" : ""}">
            {#if error.enabled}
                <p class="error-message">{error.message}</p>
            {/if}
            
            <!-- svelte-ignore a11y-missing-attribute -->
            <a class="input-button" title="clear" data-clear>
                <i class="icon-close"></i>
            </a>
        </div>
    </Flatpickr>
</div>

<style>
    label {
        font-weight: 600;
        margin-bottom: 10px;
        display: block;
        color: var(--dark-blue);
    }
    input {
        height: 51px;
        width: 100%;
        border-radius: 5px;
        outline: none;
        background-color: var(--light-grey);
        border: none;
        padding: 0 20px;
    }
    .error {
        border: 2px var(--red) solid;
    }
    .error-message {
        font: var(--primary-font-regular);
        font-size: 12px;
        color: var(--red);
        margin-bottom: 15px;
        margin-top: 5px;
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
    .flatpickr {
        margin-bottom: 15px;
    }
</style>