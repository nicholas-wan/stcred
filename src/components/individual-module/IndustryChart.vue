<script>

import jsondata from '@/data/module_data.json';


export default {
    name: 'ind-chart',
    props: {
      code: String,
    },
    data () {
        return {
            code: this.code,
            moduledata: jsondata,
            renderAt: "chart-container",
            width: "100%",
            height: "360",
            dataFormat: "json",
            type: "doughnut2d",
            datasource: {
                "chart": {
                    "caption": "Employed Industry",
                    "subCaption": "Only representative of last year's GES respondents",
                    "captionPadding": "0",
                    "chartTopMargin": "16",
                    "showpercentvalues": "1",
                    "defaultcenterlabel": "",
                    "aligncaptionwithcanvas": "0",
                    "captionpadding": "0",
                    "decimals": "1",
                    "manageLabelOverflow": "1",
                    "doughnutRadius" : "25",
                    "plottooltext": "<b>$percentValue</b> of respondent graduates work in <b>$label</b>",
                    "centerlabel": "$value", //"# Graduates: $value",
                    "theme": "fusion",
                    "showLegend": "1",
                    "bgColor": "#FAF8EA",
                    "bgAlpha": "40",
                    "legendItemFontSize" : "12",

                },
                "data": null,
            },
        }
    },
    mounted() {
      this.fillData();
    },
    methods: {
      fillData() {
        // this is where we will query the imported (json) data with the module code prop for the appropriate data
        //Replace below line with query result using module code prop, FIT THIS FORMAT (list of jsons)
        this.datasource.data = this.moduledata[this.code]['Industry']/**[{
            "label": "Healthcare",
            "value": "1323"
        }, {
            "label": "Finance",
            "value": "833"
        }, {
            "label": "Transport",
            "value": "2107"
        }]**/;
      },
    }
}
</script>

<template>
    <div id="app">
      <div id="chart-container">
        <fusioncharts
          :type="type"
          :width="width"
          :height="height"
          :dataformat="dataformat"
          :datasource="datasource"
          >
        </fusioncharts>
      </div>
    </div>
</template>


<style scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
