---
title: Frequently Asked Questions
sidebar_position: 7
---

:::info
This page needs your contribution! Please contribute new questions (or answers) using the edit link at the bottom.
:::

### Is OpenLineage a metadata server?

No. OpenLineage is, at its core, a specification for lineage metadata. But it also contains a collection of integrations, examples, and tools.

If you are looking for a metadata server that can receive and analyze OpenLineage events, check out [Marquez](https://marquezproject.ai).

### Is it possible to extract column-level data lineage from arbitrary java applications?

We have a legacy java ETL application that
* reads inputs from an RDBMS
* transforms
* filters
* aggregates
* uses Apache Ignite to store temporary values
* then writes the outcome to another RDBMS

Is it possible to extract the column-level data lineage information automatically and store in in OpenLineage/Marquez?

<span style="color:blue">TODO: add reply here</span>

### Is there room for another question on this page?

You bet! There's always room. Submit an issue or pull request using the edit button at the bottom.
