

def getEditRecordPage(instance):
    return '''
      
<div class="right_content_box">
   <div class="common-heading">
      <h4>Edt Record</h4>
   </div>
   <div class="common-content mt20">
      <div class="card max-WT-600 mrgn-0-auto">
         <div class="card-body">
            <div class="setting-page">
               <form class="commonForm" >
                  <div class="row">
                     <div class="col-md-12">
                        <div class="form-group row">
                           <label class="col-md-4 col-4 d-flex align-items-center fontbold">Name:</label>
                           <div class="col-md-8 col-8 d-flex align-items-center">
                              <input type="text" id="id_name" value="'''+ str(instance.name)+ '''" name="name" maxlength="50" class="form-control"
                                  required>
                           </div>
                           
                        </div>
                     </div>
                     <div class="col-md-12">
                        <div class="form-group row">
                           <label class="col-md-4 col-4 d-flex align-items-center fontbold">Email:</label>
                           <div class="col-md-8 col-8 d-flex align-items-center">
                              <input type="text" id="id_email" name="email" value="'''+ str(instance.email)+ '''" maxlength="50" class="form-control"
                                  required>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-12">
                        <div class="form-group row">
                           <label class="col-md-4 col-4 d-flex align-items-center fontbold">Mobile Number:</label>
                           <div class="col-md-8 col-8 d-flex align-items-center">
                              <input type="number" id="id_mobile" style="margin-left: 5px;" value="'''+ str(instance.mobile)+ '''" name="mobile" maxlength="50"
                                 class="form-control"  required>
                           </div>
                        </div>
                     </div>

                     <div class="col-md-12">
                        <div class="form-group row">
                           <label class="col-md-4 col-8 d-flex align-items-center fontbold">Gender:</label>
                           <div class="col-md-8 col-8 d-flex align-items-center">
                            <label>
                            <input type="radio" name="gender" id="male" value="Male" checked/>Male
                            </label>
                            <label>
                                <input type="radio" name="gender" id="female" value="Female"/>Female
                            </label>
                           </div>
                           <script>
                               if("'''+ str(instance.gender)+ '''" == 'Male'){
                                $("#male").prop("checked", true);
                               }else{
                                $("#female").prop("checked", true);
                               }
                           </script>
                        </div>
                     </div>
                  </div>
                  <div style="color: red;" id="id_error"></div>
                  <div class="text-center mt20">
                     <button type="button" onclick='handelEditRecord("'''+str(instance.uuid)+'''")' class="btn max-WT-180 btnGreen mr5 pTB8">Edit Record</button>
                  </div>
            </div>
         </div>
      </div>
   </div>
</div>
<script>
   var isNumberValid = true
   var isNameValid = true
   var isEmailValid = true;
   $("#id_mobile").on('keyup', function () {
      mobileValidate();
   });
   $("#id_name").on('keyup', function () {
      nameValidate();
   });
   $("#id_email").on('keyup', function () {
      emailValidate();
   });

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

   let isDigitsValidation = (digits) => {
      var re = /^\d+$/;
      if (re.test(digits)) {
         return true;
      } else {
         return false;
      }
   }
   let mobileValidate = () => {
      isNumberValid = false;
      let number = $("#id_mobile").val();
      $("#p_mobile").show();
      if (number.length === 0) {
         isNumberValid = false;
         $("#id_mobile").css('border-color', 'red');
         $("#p_mobile").text("This field is required.").css("color", "red");
         $("#p_mobile").show();
      } else {
         is_true = isDigitsValidation(number)
         if (is_true && number.length >= 10) {
            $("#id_mobile").css('border-color', 'green');
            $("#p_mobile").hide();
            isNumberValid = true;
         } else {
            isNumberValid = false;
            $("#id_mobile").css('border-color', 'red');
            $("#p_mobile").text("Phone no. Should be at least 10.").css("color", "red");
            $("#p_mobile").show();
         }
      }
   }
   function nameValidate() {
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

   let validateData = () => {
      mobileValidate();
      nameValidate();
      emailValidate();
      matchPassword();
      if (isNumberValid && isNameValid && isEmailValid && isPasswordValidate) {
         return true;
      } else {
         return false;
      }

   }


</script>
    '''