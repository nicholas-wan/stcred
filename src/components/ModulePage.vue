<template>
  <div class="module_page">
    <b-container fluid class="content">

      <b-row align-h="center">
        <b-col cols="12">
          <module-title v-bind:code="toUpperCase(code)" v-bind:name="name"></module-title>
        </b-col>
      </b-row>

      <b-row>
        <b-col class="moduleInfo" cols="4"> <!-- implied cols="4" as it is even-->
          <information v-bind:code="toUpperCase(code)" v-bind:description="description" v-bind:lessons="lessons" v-bind:breakdown="breakdown"></information>
        </b-col>

        <b-col class="chartCol" cols="4"> <!-- implied cols="4" as it is even-->
          <major-chart v-bind:code="toUpperCase(code)"></major-chart>
          <requirements-chart v-bind:code="toUpperCase(code)"></requirements-chart>
        </b-col>

        <b-col class="chartCol" cols="4"> <!-- implied cols="4" as it is even-->
          <year-chart v-bind:code="toUpperCase(code)"></year-chart>
          <industry-chart v-bind:code="toUpperCase(code)"></industry-chart>
        </b-col>
      </b-row>
    </b-container>

    <b-row>
    </b-row>

    </br></br></br></br></br>
    <Footer/>
  </div>
</template>

<script>
  import Footer from "@/components/Footer.vue";
  import title from '@/components/individual-module/ModuleTitle.vue'
  import info from '@/components/individual-module/ModuleInformation.vue';
  import major from '@/components/individual-module/MajorChart.vue';
  import year from '@/components/individual-module/YearChart.vue';
  import req from '@/components/individual-module/RequirementsChart.vue';
  import ind from '@/components/individual-module/IndustryChart.vue';
  import jsondata from '@/data/module_data.json';
  import { mapState } from 'vuex';


  export default {
    name: "batch",
    components: {
      'module-title': title,
      'information': info,
      'major-chart': major,
      'year-chart': year,
      'requirements-chart': req,
      'industry-chart': ind,
      Footer
    },
    data() {
        return {
            code: this.$store.state.code,
            capCode: '',
            moduledata: jsondata,
            name: '',
            description: '',
            lessons: [],
        }
    },
    mounted() {
      this.ensureCapitalCode();
      this.getModuleData();
    },
    methods: {
      toUpperCase(text) {
        return text.toUpperCase()
      },
      ensureCapitalCode() {
        this.capCode = this.code.toUpperCase()
      },
      getModuleData() {
        this.name = this.moduledata[this.capCode]['Name']
        this.description = this.moduledata[this.capCode]['Description']
        this.lessons = this.moduledata[this.capCode]['Lessons']
        this.breakdown = this.moduledata[this.capCode]['Breakdown']
      }
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#module_page {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}

.moduleInfo{
  text-align: left;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif; /**not working**/
}

.chartCol {
  width: 100%;
  margin-top: -20px;
}

h3 {
  margin: 40px 0 0;
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
