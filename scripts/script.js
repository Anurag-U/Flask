// // var selectedRow = null;
// // function onFormSubmit(e) {
// //     event.preventDefault();
// //     var formData =readformData();
// //     if(selectedRow === null){
// //         insertNewRecord(formData);

// //     }
// //     else{
// //         updateRecord(formData)
// //     }
// //     resetForm();
// // }

// //retreiving the data
// // function readformData() {
// //     var formData = {};

// //     formData["name"] = document.getElementById["name"].value;
// //     formData["age"] = document.getElementById["age"].value;
// //     // formData["Delete"] = document.getElementById["Delete"].value;
// //     return formData;



// // }
// //insert the data
// // function insertNewRecord(data){
// //     var table =document.getElementById("storeList").getElementsByTagName('tbody')[0] 
// //    var newRow = table.insertRow(table.length);
// //    var cell1 =newRow.insertCell(0);
// //        cell1.innerHTML=data.name;

// //    cell2 =newRow.insertCell(1);
// //    cell2.innerHTML=data.age;

// // //    cell3 =newRow.insertCell(3);
// // //    cell3.innerHTML=data.Delete;

// //     cell3 =newRow.insertCell(3);
// //     cell3.innerHTML= <button onClick='onEdit(this)'>edit_button1</button>
                



// // }

// // function updateRecords(formData){
// //     selectedRow.cells[0].innerHTML =formData.edit_button1
// //     selectedRow.cells[1].innerHTML =formData.save_button1
// //     selectedRow.cells[2].innerHTML =formData.Delete
    
// // }

// //delete the data
// function onDelete(td){
//     if (confirm('do you want to delete this record')){
//         row = td.parentElement.parentElement;
//         document.getElementById('storeList').deleteRow(row.rowIndex);
//     }
//     resetForm();
// }

// // //reset the data
// // function resetForm(){
// //     document.getElementById('name').value ='';
// //     document.getElementById('age').value ='';
//     // document.getElementById('Delete').value ='';

// // }

// // function onEdit(td) {
// //     selectedRow =td.parentElement.parentElement;
// //     print(selectedRow)
// //     document.getElementById("name").value= selectedRow.cells[0].innerHTML;
// //     document.getElementById("age").value= selectedRow.cells[1].innerHTML;

// // }

// function onClick(){
//     // console.log("clicked");
//     alert("test")
// }