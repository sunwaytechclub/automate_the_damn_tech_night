<script>
    import TextInput from "@/components/TextInput.svelte"
    import Dropdown from "@/components/Dropdown.svelte"

    import { storeFE, selectedSpeakers } from '@/components/stores.js';

    export let objAttributes = {};
    let selectedValue;
    let tempValue = ""

    function handleSelect(event) {
        let value = event.detail.value
        
        if (!$selectedSpeakers.includes(value)) {
            if (value != tempValue && tempValue !== "" && tempValue !== null) {
                $selectedSpeakers.pop()
            }
            let l = $selectedSpeakers.length;
            $selectedSpeakers[l] = value
            tempValue = value;

            $storeFE[l].selectedSpeaker = value

            return
        }

        selectedValue = null
    }
</script>

<div class="speaker-header-div">
    <p class="speaker-header">Speaker #{objAttributes.id}</p>
</div>
<div class="side-by-side">
    <TextInput label="Topic" placeholder="Topic" bind:value={objAttributes.topic}/>
    <Dropdown label="Speaker name" placeholder="Speaker name" 
        items={objAttributes.speakers} bind:selectedValue on:select={handleSelect}/>
</div>
<div>
    <TextInput label="Caption" placeholder="Caption" bind:value={objAttributes.caption}/>
</div>

<style>
    .speaker-header-div {
        position: relative;
        margin-bottom: 15px;
        margin-top: 20px;
    }
    .speaker-header {
        font: var(--primary-font-bold);
    }
    .speaker-header:after {
        position: absolute;
        top: 51%;
        left: 100px;
        overflow: hidden;
        width: 87%;
        height: 2px;
        content: '\a0';
        background-color: var(--light-grey)
    }
    .side-by-side {
        display: grid;
        grid-template-columns: auto auto;
        column-gap: 30px
    }
</style>