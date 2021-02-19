<script>
    export let icon = "/assets/icons/plus-circle-yellow.svg";
    export let label = "Add Topic";
</script>

<div class="action-div" on:click>
    <img src={icon} alt="plus"/>
    <p class="action-text">{label}</p>
</div>

<style>
    .action-div {
        display: flex;
        align-items: center;
        cursor: pointer;
    }
    .action-text {
        display: inline;
        color: var(--yellow);
        font: var(--primary-font-semibold);
        margin-left: 12px;
    }
</style>