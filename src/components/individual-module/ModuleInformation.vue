

<script>
import jsondata from '@/data/module_data.json';

export default {
  name: 'Overview',
  props: {
    code: String,
    description: String,
    lessons: Array,
  },
  mounted() {
    this.fillDescriptionData();
  },
  data () {
    return {
      code: this.code,
      description: this.description,
      lessons: this.lessons,
      moduledata: jsondata,
      renderAt: "chart-container",
      width: "100%",
      height: "300",
      dataFormat: "json",
      type: "doughnut2d",
      datasource: {
          "chart": {
              "captionPadding": "0",
              "chartTopMargin": "0",
              "alignCaptionWithCanvas": "1",
              "captionHorizontalPadding": "2",
              "captionOnTop": "0",
              "captionAlignment": "right",
              "showLabels": "0",
              "showValues": "0",
              "showpercentvalues": "1",
              "captionpadding": "0",
              "decimals": "1",
              "paletteColors": ['#F0E4C9', '#EACEC2', '#C6DBB9', '#ACBED8'],
              "showZeroPies": "0",
              "manageLabelOverflow": "1",
              "doughnutRadius" : "30",
              "plottooltext": "<b>$label</b>, $percentValue",
              "defaultcenterlabel": "",
              "centerLabelFontSize": "16",
              "centerlabel": "$percentValue",
              "theme": "fusion",
              "showLegend": "1",
              "legendItemFontSize": "12",
              //"bgColor": "#FAF8EA",
              //"bgAlpha": "40",

          },
          "data": null,
      },
    }
  },
  methods:{
      newTab: function () {
          window.open("https://nusmods.com/modules/" + this.code);
      },
      fillDescriptionData() {
        this.datasource.data = this.moduledata[this.code]['Breakdown']
      },
    }
}
</script>

<template>

  <div class="information">
    <div class="left">

      <h1 class="Title">Overview</h1>
      <body class="paragraph">
        <p class="text-justify">
          {{description}}
        </p>
      </body>

      <h1 class="Title">Lessons</h1>

      <b-container fluid class="lessons-table">
        <b-row align-h="left">

          <b-col cols="6">

            <b-row align-h="left">
            <body class="lessonCat">Lecture: </br></body>
            </b-row>
            <b-row align-h="left">
              <div v-if="lessons[0] == 0">
                <body class="lessonValue">-</body>
              </div>
              <div v-else>
                <body class="lessonValue">{{lessons[0]}} * {{lessons[1]}} hr session(s) / {{lessons[2]}} week(s)</body>
              </div>
            </b-row>

            <b-row align-h="left">
            <body class="lessonCat">Sectional:</body>
            </b-row>
            <b-row align-h="left">
              <div v-if="lessons[3] == 0">
                <body class="lessonValue">-</body>
              </div>
              <div v-else>
                <body class="lessonValue">{{lessons[3]}} * {{lessons[4]}} hr session(s) / {{lessons[5]}} week(s)</body>
              </div>
            </b-row>


            <b-row align-h="left">
            <body class="lessonCat">Recitation:</body>
            </b-row>
            <b-row align-h="left">
              <div v-if="lessons[6] == 0">
                <body class="lessonValue">-</body>
              </div>
              <div v-else>
                <body class="lessonValue">{{lessons[6]}} * {{lessons[7]}} hr session(s) / {{lessons[8]}} week(s)</body>
              </div>
            </b-row>

          </b-col>

          <b-col cols="6">

            <b-row align-h="left">
            <body class="lessonCat">Tutorial:</body>
            </b-row>
            <b-row align-h="left">
              <div v-if="lessons[9] == 0">
                <body class="lessonValue">-</body>
              </div>
              <div v-else>
                <body class="lessonValue">{{lessons[9]}} * {{lessons[10]}} hr session(s) / {{lessons[11]}} week(s)</body>
              </div>
            </b-row>

            <b-row align-h="left">
            <body class="lessonCat">Lab:</body>
            </b-row>
            <b-row align-h="left">
              <div v-if="lessons[12] == 0">
                <body class="lessonValue">-</body>
              </div>
              <div v-else>
                <body class="lessonValue">{{lessons[12]}} * {{lessons[13]}} hr session(s) / {{lessons[14]}} week(s)</body>
              </div>
            </b-row>

            <b-row align-h="left">
            <body class="lessonCatEmpty">_</body>
            </b-row>
            <b-row align-h="left">
            <body class="lessonValueEmpty">_</body>
            </b-row>

          </b-col>

        </b-row>
      </b-container>
      <b-row align-h="end" class="button">
        <!--<b-button size="sm" variant="outline-primary" @click="newTab"><div class="buttontext">Add to timetable in NUSMods</div></b-button>-->
        <button @click="newTab"><div class="buttontext">Add to timetable in NUSMods</div></button>
      </b-row>



      <h1 class="Title">Assessment Breakdown</h1>
      <div class="chartContainer">
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
  </div>

</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#box {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}

.information {
    display: grid;
    grid-template-columns: 100%;
    grid-template-rows: 100%;
    grid-template-areas:
      "left";
    height: 100%;
  }

.Title {
    color: #003d7c;
    font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
    font-weight: "bold"; /**330;**/
    font-size: 26px;
    margin: 30px auto 10px;
}

.paragraph{
    color: #424242;
    font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
    font-weight: "200"; /**330;**/
    font-size: 12px;
    text-align: "right";
    margin: 10px auto 10px;
}

.lessons-table {
  margin-left: -50px;
}

.lessonCat{
  color: #EE5230;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: 10;
  font-size: 14px;
}

.lessonValue{
  font-weight: "bold";
  font-size: 13px;
}

.lessonCatEmpty{
  color: #FFFFFF;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: 10;
  font-size: 14px;
}

.lessonValueEmpty{
  color: #FFFFFF;
  font-weight: "bold";
  font-size: 13px;
}

button {
  background: #FFFFFF;
  height: 38px;
  border: 1px;
  border-radius: 3px;
  border-color: #007BFF;
  /**
  border-radius: 2px;
  border: #fff; none
  color: #fff;
  text-emphasis-color: #E27979;
  padding: 10px;
  margin: 5px;**/
}

.buttontext {
  color: #007BFF; /**#F9F9F9;**/
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: 400; /**330;**/
  font-size: 14px;
}

.button {
  margin-top: 7px;
  /**margin-left: 50px;**/
}
</style>
