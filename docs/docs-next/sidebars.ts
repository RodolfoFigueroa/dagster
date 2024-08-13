import type { SidebarsConfig } from "@docusaurus/plugin-content-docs";

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  // docSidebar: [{ type: "autogenerated", dirName: "." }],
  docs: [
    {
      type: "category",
      label: "Getting Started",
      items: ["intro", "tutorial/quick-start", "tutorial/installation"],
    },
    {
      type: "category",
      label: "Tutorial",
      items: ["tutorial/tutorial-etl"],
    },
    {
      type: "category",
      label: "Guides",
      items: [
        {
          type: "category",
          label: "Data assets",
          link: {
            type: "doc",
            id: "guides/data-assets"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "guides/data-assets"
            }
          ]
        },
        {
          type: "category",
          label: "Transformation",
          link: {
            type: "doc",
            id: "guides/transformation"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "guides/transformation"
            }
          ]
        },
        {
          type: "category",
          label: "Automation",
          link: {
            type: "doc",
            id: "guides/automation"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "guides/automation"
            }
          ]
        },
        {
          type: "category",
          label: "External systems",
          link: {
            type: "doc",
            id: "guides/external-systems"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "guides/external-systems"
            }
          ]
        },
        {
          type: "category",
          label: "Testing",
          link: {
            type: "doc",
            id: "guides/testing"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "guides/testing"
            }
          ]
        },
        {
          type: "category",
          label: "Monitoring",
          link: {
            type: "doc",
            id: "guides/monitoring"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "guides/monitoring"
            }
          ]
        },
        {
          type: "category",
          label: "Deployment",
          link: {
            type: "doc",
            id: "guides/deployment"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "guides/deployment"
            }
          ]
        }
      ],
    },
    {
      type: "category",
      label: "Concepts",
      items: [
        {
          type: "category",
          label: "Assets",
          link: {
            type: "doc",
            id: "concepts/assets"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "concepts/assets"
            },
          ]
        },
        {
          type: "category",
          label: "Automation",
          link: {
            type: "doc",
            id: "concepts/automation"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "concepts/automation"
            },
          ]
        },
        {
          type: "doc",
          label: "Partitions",
          id: "concepts/partitions",
        },
        {
          type: "doc",
          label: "Resources",
          id: "concepts/resources",
        },
        {
          type: "doc",
          label: "I/O managers",
          id: "concepts/io-managers",
        },
        {
          type: "category",
          label: "Ops and jobs",
          link: {
            type: "doc",
            id: "concepts/ops-jobs"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "concepts/ops-jobs"
            },
          ]
        },
        {
          type: "category",
          label: "Execution",
          link: {
            type: "doc",
            id: "concepts/execution"
          },
          items: [
            {
              type: 'autogenerated',
              dirName: "concepts/execution"
            },
          ]
        }
      ],
    },
  ],
};

export default sidebars;