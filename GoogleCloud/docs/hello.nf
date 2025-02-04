#!/usr/bin/env nextflow
nextflow.enable.dsl=2 

params.str = 'Hello World'

process sayHello {
  input:
  val str

  output:
  stdout

  """
  echo $str > hello.txt
  cat hello.txt
  """
}
workflow {
  sayHello(params.str) | view
}