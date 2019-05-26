require 'json'
require 'csv'

paths = [
  '1/train_session_tue_may_21_03_35_43',
  '1/train_session_tue_may_21_04_13_01',
  '1/train_session_tue_may_21_05_07_13',
  '1/train_session_tue_may_21_05_43_24',
  '1/train_session_tue_may_21_06_39_45',
  '1/train_session_tue_may_21_07_17_14',
  'NCBI-disease-IOB/train_session_tue_may_21_02_49_59',
  'NCBI-disease-IOB/train_session_tue_may_21_03_12_48',
  'NCBI-disease-IOB/train_session_tue_may_21_03_48_35',
  'NCBI-disease-IOB/train_session_tue_may_21_07_29_27',
  'BC5CDR-IOB/train_session_tue_may_21_05_55_15',
  'BC5CDR-IOB/train_session_tue_may_21_06_17_21',
  'BC5CDR-IOB/train_session_tue_may_21_06_53_17',
  'BC5CDR-chem-IOB/train_session_tue_may_21_04_24_33',
  'BC5CDR-chem-IOB/train_session_tue_may_21_04_45_49',
  'BC5CDR-chem-IOB/train_session_tue_may_21_05_20_20'
]

paths.each { |path|
  puts "merging #{path}"

  all_epochs = File.open("./output/last/#{path}/all_epochs.json", "w")

  20.times { |n|
    epoch = (n + 1) < 10 ? "0" + (n + 1).to_s : n + 1
    all_epochs << File.open("./output/last/#{path}/epoch_0#{epoch}.txt") { |file| file.read }
  }

  all_epochs.close

  puts "success"
}

puts "DONE"
