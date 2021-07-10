const form = document.querySelector('#DonationOptionForm');
const presetAmount = document.querySelector('#presetAmount');
const userAmount = document.querySelector('#userAmount');
const donationTotal = document.querySelector('.donationTotal');
const submitButton = document.querySelector("#donationSubmit");

presetAmount.onchange = (e) => updateUserDonation(e, 'preset');
userAmount.onkeyup = (e) => updateUserDonation(e, 'user');
userAmount.onchange = (e) => updateUserDonation(e, 'user');
form.onsubmit = (e) => submitForm(e);

// change preset amount to none (0 index = no int value) if preset amount selected
const updateUserDonation = (e, option) => {

    option === 'preset'
        ? userAmount.value = ""
        : presetAmount.selectedIndex = "0";

    // get total value from user entered option
    donationTotal.value = e.target.value;

    // add disabled class if if total is zero

    if (donationTotal.value == "0" || donationTotal.value == "") {
        submitButton.disabled = true;
        submitButton.style.cursor = 'not-allowed';
    } else {
        submitButton.disabled = false;
        submitButton.style.cursor = 'pointer';
    }

    // get total and return as HTML string 
    document.getElementById('displayAmount').innerHTML = donationTotal.value;
};

// prevent form submitting if total is zero
const submitForm = (e) => {
    if (donationTotal.value === "0" || donationTotal.value === "") {
        e.preventDefault();
    } else {
        form.submit();
    }
};