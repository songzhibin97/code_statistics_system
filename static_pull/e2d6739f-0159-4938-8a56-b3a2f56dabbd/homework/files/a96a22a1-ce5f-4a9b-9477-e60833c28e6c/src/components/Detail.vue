<template>
  <div>
    <h1>{{msg}} - {{courseID}}</h1>
    <div>
      <div>{{courseDetail.title}}</div>
      <div><img v-bind:src="courseDetail.img" alt=""></div>
      <ul>
        <li v-on:click="recommendCourse(item.id)" v-for="item in courseDetail.recommends">{{item.name}}</li>
      </ul>
    </div>
    <h1>播放视频</h1>
    <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
            codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0"
            width="400" height="300" v-bind:id="'cc_'+video_brief_link">
      <param name="movie"
             v-bind:value="'https://p.bokecc.com/flash/single/C2401FCB0F73D923_'+video_brief_link + '_false_35E7C8085202EBC3_1/player.swf'"/>
      <param name="allowFullScreen" value="true"/>
      <param name="allowScriptAccess" value="always"/>
      <param value="transparent" name="wmode"/>
      <embed
        v-bind:src="'https://p.bokecc.com/flash/single/C2401FCB0F73D923_'+video_brief_link + '_false_35E7C8085202EBC3_1/player.swf'"
        width="400" height="300" name="cc_ECC9954677D8E1079C33DC5901307461" allowFullScreen="true"
        wmode="transparent" allowScriptAccess="always" pluginspage="http://www.macromedia.com/go/getflashplayer"
        type="application/x-shockwave-flash"/>
    </object>

    <h1>tab切换</h1>

    <div class="tab-menu">
      <div>
        <a v-on:click="changeTab('detail')">课程概述</a>
        <a v-on:click="changeTab('chapter')">课程章节</a>
        <a v-on:click="changeTab('review')">用户评价</a>
        <a v-on:click="changeTab('question')">常见问题</a>
      </div>
    </div>

    <div>
      <div v-show="tabs.detail">课程概述内容</div>
      <div v-show="tabs.chapter">课程章节内容</div>
      <div v-show="tabs.review">用户评价内容</div>
      <div v-show="tabs.question">常见问题内容</div>
    </div>

    <h1>价格策略</h1>
    <ul class="price-policy">
      <li v-bind:class="[{active:num==selectCourseIndex}]" v-on:click="choiceCourse(num)"
          v-for="(pri,num) in prices">¥{{pri.price}} (有效期 {{pri.period}} )
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "detail",
    data() {
      return {
        msg: '这是课程详细',
        video_brief_link: 'ECC9954677D8E1079C33DC5901307461', //3120CBCC1C598F069C33DC5901307461
        courseID: this.$route.params.id,
        courseDetail: {
          title: '',
          img: '',
          recommends: [
            {id: 2, name: '推荐课程2'},
            {id: 3, name: '推荐课程3'}
          ]
        },
        tabs: {
          detail: true,
          chapter: false,
          review: false,
          question: false,
        },
        selectCourseIndex: -1,
        prices: [
          {id: 1, price: 100, period: '2个月'},
          {id: 2, price: 200, period: '3个月'},
          {id: 3, price: 300, period: '4个月'},
        ]
      }
    },
    mounted() {
      this.init()
    },
    methods: {
      init() {
        this.initDetail()
      },
      initDetail() {
        this.courseDetail.title = "课程-" + this.courseID
        this.courseDetail.img = require("../assets/img/logo.png")
      },
      initChapter() {

      },
      initQuestion() {

      },
      recommendCourse(cid) {
        this.courseID = cid
        this.init()
      },
      changeTab: function (name) {
        for (let item in this.tabs) {
          if (item === name) {
            this.tabs[item] = true
          } else {
            this.tabs[item] = false
          }
        }
      },
      choiceCourse(index) {
        this.selectCourseIndex = index
      }
    }
  }
</script>

<style scoped>
  .tab-menu {
    border-bottom: 1px solid #ddd;
    padding-top: 30px;
    text-align: center;
  }

  .tab-menu a {
    display: inline-block;
    padding: 20px;
    border-bottom: 2px solid transparent;
    cursor: pointer;
  }

  .tab-menu a:hover {
    border-bottom: 2px solid darkseagreen;
  }

  .price-policy .active {
    background-color: darkseagreen;
  }

</style>
