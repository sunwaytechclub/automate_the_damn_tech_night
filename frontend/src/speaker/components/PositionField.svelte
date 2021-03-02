<script>
    import TextInput from "@/components/TextInput.svelte"

    import { listPositions } from '@/components/stores.js';

    export let objAttributes = {};
    export let disabled = false;

    let positionIndex = objAttributes.id - 1

    function updateValue() {
        $listPositions[positionIndex] = objAttributes.position.value
    }
</script>

<div class="speaker-header-div">
    <p class="speaker-header">Position #{objAttributes.id}</p>
</div>
<div>
    <TextInput value={$listPositions[positionIndex]} label="Position" placeholder="Position" bind:instance={objAttributes.position} {disabled} on:keyup={updateValue}/>
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
</style>