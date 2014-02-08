Morris.Area({
  element: 'morris-chart-area',
  data: [
	{ x: '2014-02-01', likes: 80 },
	{ x: '2014-02-02', likes: 78 },
	{ x: '2014-02-03', likes: 82 },
	{ x: '2014-02-04', likes: 83 },
	{ x: '2014-02-05', likes: 79 },
	{ x: '2014-02-06', likes: 85 },
	{ x: '2014-02-07', likes: 79 },
	{ x: '2014-02-08', likes: 168 },
	{ x: '2014-02-09', likes: 159 },
	{ x: '2014-02-10', likes: 142 },
	{ x: '2014-02-11', likes: 82 },
	{ x: '2014-02-12', likes: 89 },
	{ x: '2014-02-13', likes: 19 },
	{ x: '2014-02-14', likes: 49 },
	{ x: '2014-02-15', likes: 70 },
	{ x: '2014-02-16', likes: 86 },
	{ x: '2014-02-17', likes: 62 },
	{ x: '2014-02-18', likes: 64 },
	{ x: '2014-02-19', likes: 19 },
	{ x: '2014-02-20', likes: 19 },
	{ x: '2014-02-21', likes: 139 },
	{ x: '2014-02-22', likes: 190 },
	{ x: '2014-02-23', likes: 112 },
	{ x: '2014-02-24', likes: 193 },
	{ x: '2014-02-25', likes: 183 },
	{ x: '2014-02-26', likes: 148 },
	{ x: '2014-02-27', likes: 123 },
	{ x: '2014-02-28', likes: 190 },
  ],
  xkey: 'x',
  ykeys: ['likes'],
  labels: ['likes'],
  smooth: false,
});

Morris.Donut({
  element: 'morris-chart-donut',
  data: [
    {label: "TopicOne", value: 46.7},
    {label: "TopicTwo", value: 33.6},
    {label: "TopicThree", value: 10.9},
    {label: "TopicFour", value: 8.8}
  ],
  formatter: function (y) { return y + "%" ;}
});
