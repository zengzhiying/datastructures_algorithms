#!/usr/bin/env python3
# coding=utf-8
import longest_common_substring as lcs

if __name__ == '__main__':
    # 2
    print(lcs.length('AGCAT', 'GAC'))
    print(lcs.get_str('AGCAT', 'GAC'))

    # 4
    print(lcs.length("mitcmu", "mtacnu"))
    print(lcs.get_str("mitcmu", "mtacnu"))

    # 4
    print(lcs.length("kitten", "sitting"))
    print(lcs.get_str("kitten", "sitting"))

    # 8
    print(lcs.length("Never hate your enemies. If affects your judgment.", "hya y ju"))
    print(lcs.get_str("Never hate your enemies. If affects your judgment.", "hya y ju"))

    # 101 
    print(lcs.length("Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine. Write applications quickly in Java, Scala, Python, R, and SQL.",
                     "Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale."))
    print(lcs.get_str("Apache Spark achieves high performance for both batch and streaming data, using a state-of-the-art DAG scheduler, a query optimizer, and a physical execution engine. Write applications quickly in Java, Scala, Python, R, and SQL.",
                      "Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale."))
