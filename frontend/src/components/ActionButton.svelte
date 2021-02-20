<script>
    export let icon = "/assets/icons/plus-circle-yellow.svg";
    export let label = "Add Topic";
</script>

<div class="action-div">
    <img src={icon} alt="plus" on:click/>
    <p class="action-text">{label}</p>
</div>

<style>
    img {
        cursor: pointer;
    }
    .action-div {
        display: flex;
        align-items: center;
    }
    .action-text {
        display: inline;
        color: var(--yellow);
        font: var(--primary-font-semibold);
        font-size: 14px;
        margin-left: 12px;
    }
</style>