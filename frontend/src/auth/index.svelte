<script>
    import TextInput from '@/components/TextInput.svelte';
    import Button from '@/components/Button.svelte';

    let username = "";
    let password = "";
    let error;
    let errorMsg = "";
    let loading = false;

    function signIn() {
        loading = true;
        let usernameValue = username.value
        let passwordValue = password.value

        if (usernameValue == "") {
            errorMsg = "Please enter username";
            loading = false;
            return error = true;
        } else if (passwordValue == "") {
            errorMsg = "Please enter password";
            loading = false;
            return error = true;
        }
        error = false;
        // loading = false;
        
        // TODO: POST auth
        // window.location.href = "/form"

    }
</script>

<div class="wrapper">
    <div class="section-form">
        <div class="section-form-content">
            <img src="/assets/stc-logo.svg" alt="stc logo" class="logo">
            <p class="title">Sign In</p>
            <TextInput bind:value={username} disabled={loading ? true : false}/>
            <TextInput bind:value={password} disabled={loading ? true : false} label="Password" placeholder="Password" type="password"/>
            {#if error}
                <p class="error-message">{errorMsg}</p>
            {:else}
                <div class="error-spacer"></div>
            {/if}
            <Button on:click={signIn} label="Sign In" {loading}/>
        </div>
    </div>
    <div class="section-banner">
        <img src="/assets/social-media-illustration.svg" alt="illustration" class="banner-image">
        <p class="banner-title">Automate the Damn Tech Night</p>
        <p class="banner-subtext">Automate the process with just one click</p>
    </div>
</div>

<style>
    .wrapper {
        display: grid;
        grid-template-columns: 38% 62%;
        height: 100vh;
    }
    .section-form {
        display: flex;
        flex-direction: column;
        width: 100%;
        min-width: 350px;
        height: 100%;
        align-items: center;
        justify-content: center;
    }
    .section-form-content {
        width: 60%;
        min-width: 280px;
    }
    .section-banner {
        background-color: var(--purple-1);
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: left;
    }
    .logo {
        margin-bottom: 40px;
    }
    .title {
        font: var(--primary-font-bold);
        font-size: 26px;
        margin-bottom: 25px;
    }
    .banner-image {
        margin-bottom: 50px;
    }
    .banner-title {
        font: var(--primary-font-bold);
        font-size: 50px;
        color: var(--white);
        width: 500px;
        margin-bottom: 15px;
    }
    .banner-subtext {
        font: var(--primary-font-semibold);
        font-size: 16px;
        color: var(--white);
        width: 500px;
    }
    .error-message {
        font: var(--primary-font-regular);
        font-size: 12px;
        color: var(--red);
        margin-bottom: 15px;
        margin-top: -10px;
    }
    .error-spacer {
        height: 20px;
    }
</style>