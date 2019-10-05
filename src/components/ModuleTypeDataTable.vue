<template>
    <div>

      <b-row align-h="center">
      <div class="selectedHeader">
          <img v-b-popover.hover.topleft="tooltip" alt="Help" height="16" width="16" src="@/assets/help.png" />
          Selected Module:
        </div>
      </b-row>

      <b-row align-h="center">
        <div class="selectedModule">{{selectedModuleText}}</div>
      </b-row>

      <b-row align-h="center" v-show="!isInvalidInput">
        <router-link :to="{ name: 'module' }" :event="isInvalidInputR">
          <b-button @click="updateCode" variant="success" :disabled="isInvalidInput" class="searchButton"><div class="buttontext">Find Out More</div></b-button>
        </router-link>
      </b-row>

      <b-row align-h="end">
        <b-col cols="2" align-h="start">
          <div class="tableHeader" style="display: inline">
              Display rows:
              <b-form-select v-on:change="onPageSizeChanged()" v-model="selectedRowSize" size="sm">
                <option :value="10">10</option>
                <option :value="20">20</option>
                <option :value="50">50</option>
                <option :value="100">100</option>
              </b-form-select>
          </div>
        </b-col>
      </b-row>


      <b-row align-h="center">
        <b-col cols="12">
          <ag-grid-vue style="margin-top:2%;"
                      class="ag-theme-balham"
                      id="myGrid"
                      :columnDefs="columnDefs"
                      :rowData="rowData"
                      :defaultColDef="defaultColDef"
                      :gridOptions="gridOptions"
                      @grid-ready="onGridReady"
                      :pagination="true"
                      :paginationPageSize="paginationPageSize"
                      :paginationNumberFormatter="paginationNumberFormatter"
                      :floatingFilter="true"
                      :masterDetail="true"
                      rowSelection="single"
                      :sideBar="sideBar"
                      :enableRangeSelection="true"
                      :statusBar="statusBar"
                      :detailCellRendererParams="detailCellRendererParams"
                      :detailRowHeight="detailRowHeight"
                      @selection-changed="onSelectionChanged"
              >
          </ag-grid-vue>
        </b-col>
      </b-row>

    </div>
</template>


<script>
    import {AgGridVue} from "ag-grid-vue";
    import module_type_data from '../data/module_type_data.json';
    import { mapMutations } from 'vuex'

    export default {
        name: 'App',
        data() {
            return {
                selectedRowSize: "10", //default value for row/page size
                selectedModuleCode: 'None',
                selectedModuleText: 'None',
                tooltip: {
                  title: 'User Help',
                  content:
                  'Click any row in the results table to select a module. \n\n \
                  Click a column header to toggle between sorting that column in ascending/ descending order. \n\n \
                  Column widths can be adjusted. \n\n \
                  Columns can also be reordered by dragging them left/ right.'
                },
                gridOptions: null,
                gridApi: null,
                columnDefs: null,
                rowData: null,
                paginationPageSize: null,
                paginationNumberFormatter: null,
                statusBar: null,
                detailCellRendererParams: null,
            }
        },
        components: {
            AgGridVue
        },
        beforeMount() {
            this.gridOptions = {};
            this.columnDefs = [
                {headerName: 'Module Code', field: 'ModuleCode', filter: "agTextColumnFilter", width: 125, cellRenderer: "agGroupCellRenderer"},
                {headerName: 'Module Title', field: 'ModuleTitle', filter: "agTextColumnFilter", width: 130},
                {headerName: 'Module Type', field: 'Type', width: 135},
                {headerName: 'Major of Students', field: 'Major', width: 150},
                {headerName: 'Latest From', field: 'YearSem', width: 120},
                {headerName: 'Assignments %', field: 'Assignments', filter: "agNumberColumnFilter", width: 135},
                {headerName: 'Class Participation %', field: 'Class Participation', filter: "agNumberColumnFilter", width: 100},
                {headerName: 'Project Work %', field: 'Project Work', filter: "agNumberColumnFilter", width: 105},
                {headerName: 'Exams %', field: 'Exams', filter: "agNumberColumnFilter", width: 100},
                {headerName: 'Enrolment', field: 'TotalEnrolment', filter: "agNumberColumnFilter", width: 100},
            ];

            this.rowData = module_type_data;
            this.defaultColDef = { resizable: true, filter: true, sortable: true, enablePivot: true, };
            this.paginationPageSize = 10;
            this.paginationNumberFormatter = params => {
                return params.value.toLocaleString();
            };
            this.statusBar = { statusPanels: [{ statusPanel: "agAggregationComponent" }] };
            this.detailCellRendererParams = {
                detailGridOptions: {
                },
                template: function(params) {
                    var moduledesc = params.data.ModuleDescription;
                    var moduledesc = (typeof moduledesc === 'undefined') ? "Currently Unavailable" : moduledesc;

                    var word1 = params.data.Lecture;
                    var word2 = params.data.Tutorial;
                    var word3 = params.data.Lab;
                    var word4 = params.data.Project;
                    var word5 = params.data.Preparation;
                    var word6 = params.data.Graded;

                    return (
                    '<div style="padding:1%; text-align:left;">'+
                        '   <span style="white-space:normal; word-break:break-all;"> <b>Module Description:</b> '+moduledesc+'</span><br/><br/>'+
                        '   <div class="button-1">'+
                        '       <div class="eff-1"></div>'+
                        '       <a href="#/module">'+ "Find out more" +'</a>'+
                        '   </div>'+
                        '   <ul>'+
                        '       <li><h6> Expected hours per week:         </h6></li>'+
                        '       <li><div class="button-2">'+
                        '           <div class="eff-2"></div>'+
                        '           Lecture: <a href="#/">'+ word1 +'</a>'+
                        '       </div></li>'+
                        '       <li><div class="button-2">'+
                        '           <div class="eff-2"></div>'+
                        '           Tutorial: <a href="#/">'+ word2 +'</a>'+
                        '       </div></li>'+
                        '       <li><div class="button-2">'+
                        '           <div class="eff-2"></div>'+
                        '           Lab: <a href="#/">'+ word3 +'</a>'+
                        '       </div></li>'+
                        '       <li><div class="button-2">'+
                        '           <div class="eff-2"></div>'+
                        '           Project: <a href="#/">'+ word4 +'</a>'+
                        '       </div></li>'+
                        '       <li><div class="button-2">'+
                        '           <div class="eff-2"></div>'+
                        '           Preparation: <a href="#/">'+ word5 +'</a>'+
                        '       </div></li>'+
                        '       <li><div class="button-2">'+
                        '           <div class="eff-2"></div>'+
                        '           Graded: <a href="#/">'+ word6 +'</a>'+
                        '       </div></li>'+
                        '   </ul>'+
                    '</div>'
                    );
                }
            };
            this.detailRowHeight = 180;
        },
        mounted() {
            this.gridApi = this.gridOptions.api;
            this.gridColumnApi = this.gridOptions.columnApi;
        },
        methods: {
            onSelectionChanged() {
                var selectedRows = this.gridApi.getSelectedRows();
                var selectedRowsStringCode = "";
                var selectedRowsStringText = "";
                selectedRows.forEach(function(selectedRow, index) { //flexible also for multiple selection
                  if (index !== 0) {
                    selectedRowsString += ", ";
                  }
                  selectedRowsStringCode += selectedRow.ModuleCode;
                  selectedRowsStringText += selectedRow.ModuleCode + ' ' + selectedRow.ModuleTitle
                });
                this.selectedModuleCode = selectedRowsStringCode
                this.selectedModuleText = selectedRowsStringText
            },
            onPageSizeChanged(newPageSize) {
                this.gridApi.paginationSetPageSize(this.selectedRowSize); //for new row size filter
            },
            ...mapMutations([
              'UPDATE_MODULE_CODE'
            ]),
            updateCode() {
              this.UPDATE_MODULE_CODE(this.selectedModuleCode)
            }
        },
        computed: {
          isInvalidInput(){
            return (this.selectedModuleCode == 'None')
          },
          isInvalidInputR(){
            if (this.selectedModuleCode == 'None') {
              return ''
            }
            else {
              return 'click'
            }
          },
        }
    };


</script>

<style lang="scss">
    @import "../../node_modules/ag-grid-community/dist/styles/ag-grid.css";
    @import "../../node_modules/ag-grid-community/dist/styles/ag-theme-balham.css";

    .selectedHeader {
      color: #424242;
      font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
      font-weight: "330"; /**330;**/
      font-size: 27px;
      width: 100%;
      text-align: center;
      /**margin: 10px auto 10px;**/
    }

    .selectedModule {
      color: #3AAFA9 ;
      font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
      font-weight: "bold";
      font-size: 35px;
      width: 100%;
      text-align: center;
      margin-top: -5px;
      margin-bottom: 0px;
      /**margin: 10px auto 10px;**/
    }

    .tableHeader {
      color: #0c69aa;
      font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
      font-weight: 369; /**bold**/
      font-size: 16px;
      width: 100%;
      text-align: center;
      display: inline;
    }

    .searchButton {
      background: #E1E1E1;
      height: 30px;
      padding-bottom: 3px;
      padding-left: 8px;
      padding-right: 8px;
      border: #FF4040;
      border-radius: 2px;
      text-align: center;
      /**
      color: #fff;
      text-emphasis-color: #E27979;
      padding: 10px;
      margin: 5px;**/
    }

    .buttontext {
      color: #F9F9F9;
      font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
      font-weight: "bold"; /**330;**/
      font-size: 14px;
      margin-top: -2px;
    }

    .button-1{
        width:140px;
        height:30px;
        border:2px solid #21c03c;
        text-align:center;
        position:relative;
        overflow:hidden;
    }
    .button-1:hover .eff-1{
        left:0;
    }
    .eff-1{
        width:140px;
        height:30px;
        left:-140px;
        background:#21c03c;
        position:absolute;
        transition:all .5s ease;
    }
    .button-1 a{
        font-family:Helvetica;
        font-size:14px;
        color:#21c03c;
        text-decoration:none;
        line-height:30px;
        transition:all .5s ease;
        position:relative;
    }
    .button-1:hover a{
        color:#fff;
    }

    .button-2{
        width:100px;
        height:25px;
        border-radius: 25px;
        border:2px solid #1900ff;
        float:left;
        text-align:center;
        cursor:pointer;
        position:relative;
        box-sizing:border-box;
        overflow:hidden;
    }
    .button-2 a{
        font-family:Helvetica;
        font-size:10px;
        color:#1900ff;
        text-decoration:none;
        line-height:22px;
        transition:all .5s ease;
        position:relative;
    }
    .button-2:hover{
        background-color:#1900ff;
    }
    .button-2:hover a{
        color:#fff;
    }

    ul > li{
        display:inline-block;
    }

    ul {
        text-align: right;
    }
</style>
