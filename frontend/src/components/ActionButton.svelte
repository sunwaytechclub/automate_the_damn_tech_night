<script>
    export let iconPath = "/assets/icons/plus-circle-yellow.svg";
    export let label = "Add Topic";
    export let textColor = "var(--yellow)"
</script>

<div class="action-div" {...$$restProps} on:click>
    <img src={iconPath} alt="plus" />
    <p class="action-text" style="color: {textColor}">{label}</p>
</div>

<style>
    .action-div {
        cursor: pointer;
        display: flex;
        align-items: center;
        width: fit-content;
    }
    .action-text {
        display: inline;
        font: var(--primary-font-semibold);
        font-size: 14px;
        margin-left: 12px;
    }
</style>