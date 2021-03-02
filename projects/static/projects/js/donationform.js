// get select input preset 
const presetAmount = document.querySelector('#presetAmount');
// get user-entered input 
const userAmount = document.querySelector('#userAmount');
// get donation total input
const donationTotal = document.querySelector('.donationTotal');

// change user entered amount to none if preset amount selected
presetAmount.onchange = (e) => {
    userAmount.value = "";

    // get total value from preset options
    donationTotal.value = e.target.value;
    console.log(donationTotal.value);
}

userAmount.onkeyup = (e) => updateUserDonation(e)
userAmount.onchange = (e) => updateUserDonation(e)

// change preset amount to none (0 index = no int value) if preset amount selected
const updateUserDonation = (e) => {
    presetAmount.selectedIndex = "0";

    // get total value from user entered option
    donationTotal.value = e.target.value;
    console.log(donationTotal.value)

    // TBA (possible alternative to input returned total)
    // get total and return as HTML string <= currently only returning custom value
    // document.getElementById('displayAmount').innerHTML = donationTotal.value;
}