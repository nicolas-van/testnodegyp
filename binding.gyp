{
  "targets": [
    {
      "target_name": "addon",
      'include_dirs': [
        'sources',
      ],
      "sources": [ "hello.cc", "<!@(node -p \"require('fs').readdirSync('./sources').filter(f=>f.endsWith('.c')).map(f=>'sources/'+f).join(' ')\")" ]
    }
  ]
}