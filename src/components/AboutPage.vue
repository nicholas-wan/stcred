<template>
  <div class="about_page">
    <b-card
      overlay
      img-src="https://www.comp.nus.edu.sg/images/resources/20190215_Yale_NUS_and_NUS_Computing_CDP.jpg"
      img-alt="Card Image"
      text-variant="white"
      title="Frequently Asked Questions"
      title-tag="h1"
      img-height="350px"
    >

    </b-card>
    <b-container fluid class="content">
      <b-row align-h="center">
        <b-col cols="12" class="titlePosition">

  <div role="tablist">
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle.accordion1 variant="dark">What is Modules+?</b-button>
      </b-card-header>
      <b-collapse id="accordion1" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
          <p class="card-text">Modules+ is a web application designed to be complementary
                      to existing module planners such as NUSMods and NUSTimetable Builder.
                      We intend for this to app to be fit in together with NUS' official timetable builder.
                      Feedback and suggestions on improvements to the app are more than welcome!</p>
        </b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle.accordion2 variant="primary">How can I use the Course Page?</b-button>
      </b-card-header>
      <b-collapse id="accordion2" accordion="my-accordion" role="tabpanel">
        <b-card-body><p class="card-text">
          1. Get to know when your seniors have completed a module to find out if you are taking a module too early or too late. <br>
          2. Plan when to take your modules, especially if you want to take modules together with friends or peers, or if the module has group work.<br>
          3. Get to know popular module choices by seniors if you have options to choose core modules (e.g MA1521 and MA1102R for computing students)<br>
          4. Get to know popular UE’s your seniors have taken

        </p></b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle.accordion3 variant="primary">How can I use the Module Type Page?</b-button>
      </b-card-header>
      <b-collapse id="accordion3" accordion="my-accordion" role="tabpanel">
        <b-card-body><p class="card-text">
          1. Want to take a language module but not sure of the options? Look at popular choices, as well as their demographic information, such as faculty and year composition to better help you make your decision!<br>
          2. Want to know which are popular / unpopular GE modules to fulfil your requirements? <br>
          3. Get to know popular programme electives to help you to decide which modules to take for your basket modules.
        </p></b-card-body>
      </b-collapse>
    </b-card>

    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle.accordion4 variant="primary">How can I use the Industry Page?</b-button>
      </b-card-header>
      <b-collapse id="accordion4" accordion="my-accordion" role="tabpanel">
        <b-card-body><p class="card-text">
          1. Discover which modules have been taken by recent graduates in an industry. <br>
          2. Data is taken from the most recent Graduate Employment Survey.
        </p></b-card-body>
      </b-collapse>
    </b-card>
  </div>
</b-col>
      </b-row>

      <b-row align-h="center" class="description">
        <b-col cols="9">

        </b-col>
      </b-row>
    </b-container>
    </br></br></br>

    <Footer/>
  </div>
</template>

<script>
  import Footer from "@/components/Footer.vue";
  export default {
    name: "batch",
    components: {
      Footer
    }
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.titlePosition {
  color: #003d7c;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "bold";
  font-size: 56px;
  width: 100%;
  text-align: center;
  margin-top: 50px;
  padding-bottom: 0px;
}

.moduleTitle {
  color: #003d7c;
  font-family: -apple-system, BlinkMacSystemFont, Helvetica Neue, Helvetica, Arial, sans-serif;
  font-weight: "bold";
  font-size: 56px;
  width: 100%;
  text-align: center;
  margin-top: 0px;
  margin-left: 0px;
  padding-bottom: 0px;
  padding-left: 0px;
}

.shiftLeft {
  padding-right: 15px;
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
/* ---------CSS for banner------------- */
.card-img{
  object-fit:cover;
  object-position:center;
  filter: brightness(40%);
}
h1{
  color:white;
  margin-top:9rem;
  font-size:4rem;
}
.cart-text{
  font-size:2rem;
}
p{
  font-size:1.2rem;
  font-weight:400;
  text-align:left;
  color:#69707a;
  font-family:sans-serif;
  line-height:1.5;
}

a[data-v-7e99b488] {
    color: white;
    font-size:1.2rem;
    font-weight:400;

}
</style>
