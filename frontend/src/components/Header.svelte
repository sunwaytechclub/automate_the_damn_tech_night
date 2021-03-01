<script>
    import pushState from "@/utils/pushState.js"
    
    export let title = "Header"
    export let previousPath = ""

    function goBack() {
        pushState(previousPath)
    }
</script>

<div class="wrapper">
    {#if previousPath != ""}
        <img src="/assets/icons/chevron-big-left.svg" alt="" class="back-button" on:click={goBack}/>
    {/if}
    <p class="header">{title}</p>
</div>

<style>
    .wrapper {
        width: 100%;
        display: flex;
        align-items: center;
        margin-bottom: 30px;
    }
    .header {
        color: var(--dark-blue);
        font: var(--primary-font-bold);
        font-size: 35px;
    }
    .back-button {
        width: 30px;
        margin-right: 10px;
        cursor: pointer;
    }
</style>