
var isNameValid = false;
var isNumberValid = false;
var isEmailValid = false;
var isMerchantValidate = false;
var isPasswordValidate = false;
$("#id_name").on('keyup', function () {
    nameValidate();
});
$("#id_merchant").on('keyup', function () {
    merchantValidate();
});
$("#id_mobile").on('keyup', function () {
    mobileValidate();
});
$("#id_email").on('keyup', function () {
    emailValidate();
});
$("#confirm_password").on('keyup', function () {
    matchPassword();
    newPasswordValidate();
});
$("#password").on('keyup', function () {
    let len = ($("#confirm_password").val()).length;
    if (len != 0) {
        passwordValidate();
        matchPassword();

    } else {
        passwordValidate();
    }

});

let merchantValidate = () => {
    let merchant = $("#id_merchant").val();
    $("#p_merchant").show();
    isMerchantValidate = false;
    if (merchant.length === 0) {
        $("#id_merchant").css('border-color', 'red');
        $("#p_merchant").text("This field is required.").css("color", "red");
        $("#p_merchant").show();
    } else {
        isMerchantValidate = true;
        $("#p_merchant").hide();
        $("#id_merchant").css('border-color', 'green');
    }

}
let isDigitsValidation = (digits) => {
    var re = /^\d+$/;
    if (re.test(digits)) {
        return true;
    } else {
        return false;
    }
}
let nameValidate = () => {
    isNameValid = false;
    let name = $("#id_name").val();
    var regex = /^[a-zA-Z ]*$/;
    var regex_1 = /^(\w+\s?)*\s*$/;
    if (regex_1.test(name)) {
        if (regex.test(name)) {
            if (name.length < 2) {
                isNameValid = false;
                $("#id_name").css('border-color', 'red');
                $("#p_name").text("This field is required.").css("color", "red");
                $("#p_name").show();

            } else if (name.length >= 40) {
                isNameValid = false;
                $("#id_name").css('border-color', 'red');
                $("#p_name").text("Name can't be 40 Character above.").css("color", "red");
                $("#p_name").show();
            } else {
                isNameValid = true;
                $("#id_name").css('border-color', 'green');
                $("#p_name").text(" ").css("color", "green");
                $("#p_name").hide();
            }
        } else {
            $("#id_name").css('border-color', 'red');
            $("#p_name").text(" Name Should be alphabet.").css("color", "red");
            $("#p_name").show();
        }
    } else {
        $("#id_name").css('border-color', 'red');
        $("#p_name").text(" Multiple spaces and special character are not allowed.").css("color", "red");
        $("#p_name").show();
    }
}

let mobileValidate = () => {
    isNumberValid = false;
    let number = $("#id_mobile").val();
    $("#p_number").show();
    if (number.length === 0) {
        isNumberValid = false;
        $("#id_mobile").css('border-color', 'red');
        $("#p_number").text("This field is required.").css("color", "red");
        $("#p_number").show();
    } else {
        is_true = isDigitsValidation(number)
        if (is_true && number.length <= 20) {
            $("#id_mobile").css('border-color', 'green');
            $("#p_number").hide();
            isNumberValid = true;
        } else {
            isNumberValid = false;
            $("#id_mobile").css('border-color', 'red');
            $("#p_number").text("Phone no Should be at least 15.").css("color", "red");
            $("#p_number").show();
        }
    }
}

let emailValidate = () => {
    let email = $("#id_email").val();
    isEmailValid = false;
    var emailRe = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    $("#p_email").show();
    if (email.length == 0) {
        isEmailValid = true;
        $("#id_email").css('border-color', 'red');
        $("#p_email").text("This field is required.").css("color", "red");
        $("#p_email").show();
    } else {
        if (emailRe.test(email)) {
            isEmailValid = true;
            $("#id_email").css('border-color', 'green');
            $("#p_email").hide();
        } else {
            isEmailValid = false;
            $("#id_email").css('border-color', 'red');
            $("#p_email").text("Please enter a valid email id.").css("color", "red");
            $("#p_email").show();
        }
    }
}


let passwordValidate = () => {
    let password = $("#password").val();
    let lowerCaseFilter = /[a-z]/g;
    let upperCaseFilter = /[A-Z]/g;
    let digitsFilter = /[0-9]/g;
    let specialFilter = /[`~!@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi;
    let isLower = false;
    let isUpper = false;
    let isDigit = false;
    let isSpecial = false;
    $("#p_new_password").show();

    isEight = false;
    isPasswordValidate = false;
    if (lowerCaseFilter.test(password)) {
        isLower = true;
    } else {
        isLower = false;
    }

    if (upperCaseFilter.test(password)) {
        isUpper = true;
    } else {
        isUpper = false;
    }

    if (digitsFilter.test(password)) {
        isDigit = true;
    } else {
        isDigit = false;
    }

    if (specialFilter.test(password)) {
        isSpecial = true;
    } else {
        isSpecial = false;
    }
    if (isLower == false) {
        $('#p_new_password').text("Must contain a Lower letter").css("color", "red");
        $("#password").css('border-color', 'red');
    } else if (isUpper == false) {
        $('#p_new_password').text("Must contain a Capital letter").css("color", "red");
        $("#password").css('border-color', 'red');
    } else if (isDigit == false) {
        $('#p_new_password').text("Must contain a Digits").css("color", "red");
        $("#password").css('border-color', 'red');
    } else if (isSpecial == false) {
        $('#p_new_password').text("Must contain a Special letter").css("color", "red");
        $("#password").css('border-color', 'red');
    }

    if (isLower == true && isUpper == true && isDigit == true && isSpecial == true) {
        if (password.length >= 8) {
            isEight = true;
        } else {
            $('#p_new_password').text("Password should be 8 letter!").css("color", "red");
            isEight = false;
        }
    }
    if (isEight == true) {
        isPasswordValidate = true
        $('#p_new_password').text("Valid Password").css("color", "green");
        $("#password").css('border-color', 'green');
        $("#p_new_password").hide();
    }
}


let matchPassword = () => {
    isMatchedPassword = false;
    let con_pass = $("#confirm_password").val();
    let pass = $("#password").val();
    $('#p_confirm_password').show();
    if (con_pass != '' || pass != '') {
        if (con_pass === pass && isEight) {
            isMatchedPassword = true;
            $('#p_new_password').text("Password match").css("color", "green");
            $('#p_confirm_password').text("Password match").css("color", "green");
            $("#password").css('border-color', 'green');
            $("#confirm_password").css('border-color', 'green');
            $('#p_confirm_password').hide();
        } else {
            $('#p_new_password').text("Password doesn't match.").css("color", "red");
            $('#p_confirm_password').text("Confirm Password doesn't match.").css("color", "red");
            isMatchedPassword = false;
            $("#password").css('border-color', 'red');
            $("#confirm_password").css('border-color', 'red');
        }
    } else {
        $('#p_new_password').text("Password can't be empty").css("color", "red");
        $('#p_confirm_password').text("Confirm Password can't be empty").css("color", "red");
        $("#password").css('border-color', 'red');
        $("#confirm_password").css('border-color', 'red');
        isMatchedPassword = false;
    }
}

let submitData = () => {
    mobileValidate();
    emailValidate()
    nameValidate()
    matchPassword()
    merchantValidate()
    if (isNameValid && isEmailValid && isMerchantValidate && isMobileValid && isNumberValid && isMatchedPassword) {
        return true;
    } else {
        return false;
    }
}

let passwordData = () => {
    if (isMatchedPassword) {
        return true;
    } else {
        return false;
    }

}