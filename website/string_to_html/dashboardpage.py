def hasPrevious(queary):
    if queary.has_previous:
        print(queary.previous_page_number)
        return '''
            <a class="page-link" href="?page='''+ str(queary.previous_page_number) +'''" aria-label="Previous">
                <span aria-hidden="true">«</span>
                <span class="sr-only">Previous</span>
            </a> 
        '''
                        
def currentPage(queary):
    current=''
    for num in queary.paginator.page_range:
        if queary.number == num:
            current+='''
                    <li class="page-item active">
                        <a class="page-link" href="?page='''+str(num)+'''">'''+str(num)+'''</a>
                    </li>
                    '''
        else:
            current+='''<li class="page-item">
                <a class="page-link" href="?page='''+str(num)+'''">'''+str(num)+'''</a>
            </li>'''
    return current

def hasNext(queary):
    if queary.has_next:
        return '''<a class="page-link" href="?page=''' + str(queary.next_page_number)+'''" aria-label="Next">
            <span aria-hidden="true">»</span>
            <span class="sr-only">Next</span>
        </a>'''

def getDashboardPage(queary):
    table = '''
    <div class="right_content_box">
    <div class="common-heading">
        <h4>User Management</h4>
        <div class="form-group">
            <div class="form-group" style="padding-left: 5px;">
                    <button onclick="switchAddrecordPage()" type="submit" class="btn btnGreen">Add
                        Record</button>
                </div>
        </div>
    </div>
    <div class="common-content mt20">
        <div class="table-responsive">
            <table id="participant_table" class="table table-bordered table-common mt15">
                <thead>
                    <tr>
                        <th>Sr No.</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>

    '''
    if queary:
        sl=1
        for data in queary:
            table +='''<tr>
                        <td>'''+ str(sl) +'''</td>
                        <td>''' + str(data.name) +'''</td>
                        <td>''' + str(data.email) + '''</td>
                        <td class="action_td_btn5">
                            <i onclick='switchViewPage("'''+str(data.uuid)+'''")' class="fa fa-eye" style="font-size:18px"></i>
                           
                                    <i onclick='switchEditPage("'''+str(data.uuid)+'''")' class="fa fa-edit edit-icon" style="font-size:18px">
                                     </i>
                            
                            <a href="#deleteUserModal_'''+str(data.uuid)+'''" data-toggle="modal"> <i class="fa fa-trash-o"
                                    style="font-size:18px"></i></a>
                            <!-- Modal Start-->
                            <div class="modal fade global-modal" id="deleteUserModal_'''+str(data.uuid)+'''">
                                <div class="modal-dialog max-WT-450">
                                    <div class="modal-content">
                                        <div class="modal-header justify-content-center pb0">
                                            <h4 class="modal-title pb0">Delete</h4>
                                        </div>
                                        <hr>
                                        <div class="modal-body pt0">
                                            <div class="row align-items-center min-ht-200">
                                                <div class="col">
                                                    <div class="form-box">
                                                        <div class="form-group text-center">
                                                            <p class="mTB30 font-16">Are you sure you want to delete
                                                                this queary?</p>
                                                        </div>
                                                        <div class="action-btn text-center">
                                                            <button onclick='handelDelete("'''+ str(data.uuid) +'''")'
                                                                class="btn max-WT-100 btnGreen mr5 pTB10">Yes</button>
                                                            <button type="button"
                                                                class="btn max-WT-100 btnGray mt0 pTB10"
                                                                data-dismiss="modal">No
                                                            </button>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </td>
                    </tr>

            '''
            
            sl+=1
    #     if queary.has_other_pages:
    #         table+='''
    #                 <div class="custom-pagination mt20 text-right">
    #     <nav aria-label="Page navigation example">
    #         <ul class="pagination">
    #             <li class="page-item">
    #             '''+str(hasPrevious(queary)) +'''
    #             </li>
    #             '''+str(currentPage(queary))+'''
    #             <li class="page-item">
    #                 '''+str(hasNext(queary))+'''
    #             </li>
    #         </ul>
    #     </nav>
    # </div>'''
    else:
        table+='''<tr>
                        <td colspan="8" style="text-align:center">Data not found.</td>
                    </tr>
                </tbody>
            </table>
        </div>
        '''
    return table
