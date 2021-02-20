<script>
    export let checked = false;
    export let label = "Checkbox"
    export let subText = ""

    function handleCheck() {
        checked = !checked
    }
</script>
<div class="wrapper">
    <div class="checkbox-div">
        <img src="/assets/icons/circle-{checked ? "check-yellow" : "yellow"}.svg" alt="unchecked icon" on:click={handleCheck}/>
        <p class="checkbox-text">{label}</p>
    </div>
    {#if subText}
        <p class="checkbox-subtext">{subText}</p>
    {/if}
</div>
<style>
    .wrapper {
        margin-bottom: 15px;
    }
    .checkbox-div {
        display: flex;
        align-items: center;
    }
    .checkbox-div img {
        cursor: pointer;
    }
    .checkbox-text {
        display: inline;
        color: var(--yellow);
        font: var(--primary-font-semibold);
        font-size: 14px;
        margin-left: 12px;
    }
    .checkbox-subtext {
        color: var(--purple-1);
        font: var(--primary-font-regular);
        font-size: 10px;
        margin-left: 36px;
    }
</style>