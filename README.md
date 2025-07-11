# ANDless

## Purpose
Despite the long-standing utility of tools like Logic Friday, the space of digital logic minimization software remains outdated and underpowered. Existing solutions often suffer from:
- Abandoned development or restrictive licensing
- Incompatibility with modern platforms (e.g., Logic Friday is Windows-only)
- Limited support for modern algorithms (typically only Espresso)
- Outdated UI or CLI only

ANDless aims to address these issues with a modern, open-source digital logic minimization framework that is:
- Cross-platform (Linux, Windows, macOS)
- Algorithmically extensible
- UI-modern (native frontends using platform-specific tools like SwiftUI or GTK)
- Designed for education, analysis, and prototyping
- Featuring standard interactive tools such as truth tables and drag-and-drop editing

Beyond basic minimization, ANDless will support:
- Custom gate libraries for macro-level abstraction
- Constraint-aware synthesis (e.g., gate delays, fan-in limits)
- Circuit equivalence checking
- Exportable logic formats (e.g., Verilog modules, truth tables, schematics)
- AND much more

Unlike industry tools such as Intel’s Quartus, ANDless will provide:
- Direct support for logic-level design and industry-standard HDL integration, easing the learning curve
- Full customizability of minimization algorithms for research and education

My initial target platform is Linux, focusing on a CLI-first design with gradual expansion to full-featured native frontends. ANDless will be built from the ground up for maintainability and community collaboration. ANDless is not intended to replace massive commercial syntåhesis suites but rather to bridge the gap between hardware engineering education and professional design tools.

## Technical Stack
### Linux
- **Backend**
  - Python
- **Frontend**
  - TBD
- **Tools**
  - Git