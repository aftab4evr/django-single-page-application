

def getViewDetailPage(instance):
    return '''
<div class="right_content_box">
   <div class="common-heading">
      <h4>View Record</h4>
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
                              <label>'''+ str(instance.name)+'''</label>
                           </div>
                           
                        </div>
                     </div>
                     <div class="col-md-12">
                        <div class="form-group row">
                           <label class="col-md-4 col-4 d-flex align-items-center fontbold">Email:</label>
                           <div class="col-md-8 col-8 d-flex align-items-center">
                            <label>'''+ str(instance.email)+'''</label>
                           </div>
                        </div>
                     </div>
                     <div class="col-md-12">
                        <div class="form-group row">
                           <label class="col-md-4 col-4 d-flex align-items-center fontbold">Mobile Number:</label>
                           <div class="col-md-8 col-8 d-flex align-items-center">
                            <label>'''+ str(instance.mobile)+'''</label>
                              
                        </div>
                        </div>
                     </div>

                     <div class="col-md-12">
                        <div class="form-group row">
                           <label class="col-md-4 col-4 d-flex align-items-center fontbold">Gender:</label>
                           <div class="col-md-8 col-8 d-flex align-items-center">
                            <label>'''+ str(instance.gender)+'''</label>

                           </div>
                           
                        </div>
                     </div>
                  </div>
            </div>
         </div>
      </div>
   </div>
</div>
    '''