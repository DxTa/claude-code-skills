# Design patterns

A pattern names a recurring pressure and its trade-offs. Start with direct code; use one of these patterns only when its boundary, variation, or lifecycle cost is demonstrated. Catalog baseline: [Refactoring.Guru design-pattern catalog](https://refactoring.guru/design-patterns/catalog).

## Contents

- [Creational](#creational)
- [Structural](#structural)
- [Behavioral](#behavioral)

## Creational

### Factory Method

- **Intent:** Let a creator-owned extension point decide which product implementation to construct.
- **Pressure/participants:** A stable workflow needs products whose concrete type varies; Creator calls a factory operation, concrete creators provide products behind a product contract.
- **Use/reject:** Use when subclass/implementation ownership of creation is real and recurring. Prefer a function, registry, or injected constructor for one local choice.
- **Trade-offs/proof:** Localizes creation but couples it to a hierarchy. Contract-test every creator and product, including unknown/configuration failures.
- **Pseudocode:**
  ```text
  interface Exporter { write(data) }
  class Job { method run(data) { exporter().write(data) } }
  class CsvJob extends Job { method exporter() { return CsvExporter() } }
  ```
- **Source:** [Factory Method](https://refactoring.guru/design-patterns/factory-method)

### Abstract Factory

- **Intent:** Create compatible families of related products without exposing concrete classes to clients.
- **Pressure/participants:** Multiple product kinds vary as a family; client consumes product interfaces, factory supplies matching products, concrete factories encode compatibility.
- **Use/reject:** Use when mixing products from different families would be invalid and families multiply. Prefer a product bundle or functions when there is one product or no compatibility rule.
- **Trade-offs/proof:** Protects family consistency but adds interfaces and indirection. Run a compatibility matrix and an unknown-family test.
- **Pseudocode:**
  ```text
  interface Widgets { button(); menu() }
  class LightWidgets implements Widgets { button() -> LightButton(); menu() -> LightMenu() }
  class DarkWidgets implements Widgets { button() -> DarkButton(); menu() -> DarkMenu() }
  render(factory: Widgets) { draw(factory.button()); draw(factory.menu()) }
  ```
- **Source:** [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)

### Builder

- **Intent:** Separate readable, validated construction steps from the final object representation.
- **Pressure/participants:** Construction has meaningful order, optional parts, or invariants; director/client selects steps, builder assembles, product is final output.
- **Use/reject:** Use when construction rules deserve names or prevent invalid states. Prefer a keyword-only constructor, record, or staged functions for plain data.
- **Trade-offs/proof:** Makes assembly explicit but introduces mutable intermediate state. Test valid/invalid order, defaults, final invariants, and reuse/reset behavior.
- **Pseudocode:**
  ```text
  request = RequestBuilder()
    .method("POST")
    .header("Accept", "json")
    .body(payload)
    .build()  // validates once; returns immutable Request
  ```
- **Source:** [Builder](https://refactoring.guru/design-patterns/builder)

### Prototype

- **Intent:** Create a configured object by copying a registered or supplied exemplar.
- **Pressure/participants:** Replaying complex setup is costly or variant configuration is data-driven; client requests a copy, prototype defines copy semantics.
- **Use/reject:** Use when copy semantics are explicit and useful. Prefer a factory or `copy` primitive when the object owns external resources or deep ownership is unclear.
- **Trade-offs/proof:** Reuses configuration but makes aliasing and copy depth part of the contract. Test mutable nested state, identity, and resource ownership.
- **Pseudocode:**
  ```text
  template = Report(style="compact", sections=[...])
  report = template.clone()
  report.sections.add(new_section)  // template remains unchanged
  ```
- **Source:** [Prototype](https://refactoring.guru/design-patterns/prototype)

### Singleton

- **Intent:** Enforce one shared instance across a defined scope and lifecycle.
- **Pressure/participants:** A process-wide resource truly has one owner; accessor/lifecycle manager returns the shared instance.
- **Use/reject:** Use rarely for genuinely process-wide resources with explicit reset/cleanup. Prefer module state, dependency injection, or a scoped object; never use it to hide dependencies.
- **Trade-offs/proof:** Easy access costs test isolation, configuration clarity, and concurrency control. Prove lifetime, cleanup, parallel tests, and failure recovery.
- **Pseudocode:**
  ```text
  class Metrics { /* runtime supplies atomic once initialization */ }
  metrics = initialize_once(Metrics)
  getMetrics() -> metrics
  ```
- **Source:** [Singleton](https://refactoring.guru/design-patterns/singleton)

## Structural

### Adapter

- **Intent:** Translate one interface or data shape into the contract expected by existing client code.
- **Pressure/participants:** A legacy/vendor service cannot match a local interface; client uses target contract, adapter wraps adaptee and translates calls/data.
- **Use/reject:** Use at a stable compatibility boundary. Prefer one direct conversion when no reusable contract or multiple call sites exist.
- **Trade-offs/proof:** Isolates external change but can hide lossy conversion and failure semantics. Contract-test representative inputs, errors, and version changes.
- **Pseudocode:**
  ```text
  interface Store { save(record) }
  class VendorAdapter implements Store {
    service
    save(record) { service.put(toVendorRecord(record)) }
  }
  ```
- **Source:** [Adapter](https://refactoring.guru/design-patterns/adapter)

### Bridge

- **Intent:** Let an abstraction and its implementation vary independently through composition.
- **Pressure/participants:** Two change axes would otherwise multiply subclasses; abstraction holds implementation, both expose separate contracts.
- **Use/reject:** Use when both axes have independent variants. Prefer direct delegation while one axis is fixed or a second combination does not exist.
- **Trade-offs/proof:** Prevents hierarchy multiplication but adds indirection. Test the variant matrix and ensure invalid combinations are rejected.
- **Pseudocode:**
  ```text
  interface Renderer { draw(shape) }
  class Shape { renderer; draw() { renderer.draw(this) } }
  shape = Circle(renderer=SvgRenderer())
  ```
- **Source:** [Bridge](https://refactoring.guru/design-patterns/bridge)

### Composite

- **Intent:** Give leaves and containers one contract so clients can operate on a tree uniformly.
- **Pressure/participants:** Parts and groups share operations; component is the contract, leaf performs work, composite delegates to children.
- **Use/reject:** Use for a real tree with recursive operations. Prefer plain data plus traversal when nodes have no behavior or the structure is shallow.
- **Trade-offs/proof:** Simplifies callers but requires clear empty, failure, ownership, and cycle semantics. Test leaf, empty group, nested group, and cycle boundary.
- **Pseudocode:**
  ```text
  interface Node { cost() }
  class Item implements Node { cost() -> price }
  class Bundle implements Node { children; cost() -> sum(child.cost() for child in children) }
  ```
- **Source:** [Composite](https://refactoring.guru/design-patterns/composite)

### Decorator

- **Intent:** Add composable behavior around an object while preserving its contract.
- **Pressure/participants:** Orthogonal concerns such as logging, authorization, retry, or caching vary independently; decorator wraps component and delegates.
- **Use/reject:** Use when wrappers compose and ordering is meaningful. Prefer a direct call or one explicit helper when there is no independent concern.
- **Trade-offs/proof:** Supports open composition but obscures order, latency, identity, and errors. Test wrapper order, failures, and contract preservation.
- **Pseudocode:**
  ```text
  service = Timed(Authorized(Cached(real_service)))
  result = service.execute(request)
  ```
- **Source:** [Decorator](https://refactoring.guru/design-patterns/decorator)

### Facade

- **Intent:** Offer a small stable entry point over a complex subsystem workflow.
- **Pressure/participants:** Callers repeat multi-object sequencing or must know invalid internal combinations; facade owns use-case ordering and delegates subsystem work.
- **Use/reject:** Use for a real use-case boundary. Prefer direct calls when it only renames one operation; split it when it becomes a god object.
- **Trade-offs/proof:** Reduces coupling but may hide useful capability and failure detail. Test the workflow, each surfaced failure, and transaction/cleanup behavior.
- **Pseudocode:**
  ```text
  class Checkout {
    payment, inventory, shipping
    place(order) {
      inventory.reserve(order)
      payment.charge(order.total)
      return shipping.schedule(order)
    }
  }
  ```
- **Source:** [Facade](https://refactoring.guru/design-patterns/facade)

### Flyweight

- **Intent:** Share repeated immutable intrinsic state while supplying variable context externally.
- **Pressure/participants:** Many objects repeat expensive state and measured memory cost matters; factory/cache owns shared flyweights, clients provide extrinsic state.
- **Use/reject:** Use only after measurement when identity is irrelevant and state is safely immutable. Prefer ordinary objects until memory pressure is proven.
- **Trade-offs/proof:** Saves memory but introduces cache lifetime, eviction, and contention. Benchmark memory and test that mutable context never leaks through shared state.
- **Pseudocode:**
  ```text
  glyph = GlyphCache.get(font="Inter", size=12)  // shared immutable shape
  glyph.draw(canvas, position, color)             // per-use context
  ```
- **Source:** [Flyweight](https://refactoring.guru/design-patterns/flyweight)

### Proxy

- **Intent:** Control or defer access to another object while preserving the client-facing contract.
- **Pressure/participants:** Lazy loading, access policy, caching, logging, or remote access must be inserted at a stable boundary; proxy holds subject and forwards/controls.
- **Use/reject:** Use when access semantics are independent and contract-compatible. Prefer an explicit client when remote latency, retries, or authorization are core business behavior.
- **Trade-offs/proof:** Centralizes access policy but can make expensive/failing work look local. Test denied, unloaded, timeout, cache, and retry behavior.
- **Pseudocode:**
  ```text
  class LazyDocument implements Document {
    real = null
    open() { if real == null { real = load() }; return real.open() }
  }
  ```
- **Source:** [Proxy](https://refactoring.guru/design-patterns/proxy)

## Behavioral

### Chain of Responsibility

- **Intent:** Pass a request through ordered independent handlers until one handles it or the chain ends.
- **Pressure/participants:** Handler order and fall-through are policy and handlers should not know all alternatives; client starts chain, handlers decide continue/stop.
- **Use/reject:** Use for extensible in-process pipelines. Prefer a direct sequence when every step always runs or order is fixed and obvious.
- **Trade-offs/proof:** Decouples handlers but makes control flow and unhandled requests less visible. Test order, short-circuit, fall-through, and errors.
- **Pseudocode:**
  ```text
  for handler in [Cache, Auth, Route]:
    result = handler.try_handle(request)
    if result.handled: return result
  return NotFound
  ```
- **Source:** [Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)

### Command

- **Intent:** Represent an operation as an object/value so its execution can be queued, retried, audited, undone, or serialized.
- **Pressure/participants:** Work has a lifecycle beyond an immediate call; command stores receiver/arguments, invoker schedules, receiver performs.
- **Use/reject:** Use when work identity and lifecycle matter. Prefer a callable/direct call when execution is synchronous and one-shot.
- **Trade-offs/proof:** Enables history and queues but requires idempotency, serialization, and failure policy. Test replay, duplicate, failure, and undo/compensation where applicable.
- **Pseudocode:**
  ```text
  command = ChargeCard(account, amount)
  queue.push(command)
  worker.run(command)  // command.execute(); record result
  ```
- **Source:** [Command](https://refactoring.guru/design-patterns/command)

### Iterator

- **Intent:** Traverse a collection without exposing its representation or traversal state.
- **Pressure/participants:** Consumers need a stable traversal contract across representations; aggregate creates iterator, iterator tracks position.
- **Use/reject:** Use for lazy, stateful, or representation-independent traversal. Prefer the language iterator protocol/generator over a custom hierarchy.
- **Trade-offs/proof:** Supports laziness and composition but needs clear lifetime and side-effect semantics. Test empty, partial, repeat, exhaustion, and close behavior.
- **Pseudocode:**
  ```text
  iterator = tree.depth_first()
  while iterator.has_next(): consume(iterator.next())
  ```
- **Source:** [Iterator](https://refactoring.guru/design-patterns/iterator)

### Mediator

- **Intent:** Centralize complex peer coordination so participants do not maintain many direct links.
- **Pressure/participants:** Peer interactions form a changing graph with a real coordination owner; colleagues notify mediator, mediator applies rules.
- **Use/reject:** Use when coordination rules are substantial and shared. Prefer direct calls when mediator would only forward or become a god object.
- **Trade-offs/proof:** Reduces peer coupling but centralizes flow and can hide dependencies. Test an interaction matrix, ordering, and failure propagation.
- **Pseudocode:**
  ```text
  class FormMediator {
    changed(field) {
      if field == country: city.enable(country.value != null)
      if field == submit: submit_if_valid()
    }
  }
  ```
- **Source:** [Mediator](https://refactoring.guru/design-patterns/mediator)

### Memento

- **Intent:** Capture and restore state without exposing the object’s internal representation.
- **Pressure/participants:** Undo, checkpoints, or transaction rollback need snapshots; originator creates/restores, caretaker stores, memento is opaque/immutable.
- **Use/reject:** Use when snapshot boundaries are clear. Prefer targeted fields or an event log when state is huge, external, or copy ownership is uncertain.
- **Trade-offs/proof:** Simplifies restore but costs memory and copy time. Test mutate-restore, nested snapshots, alias isolation, and failed restore.
- **Pseudocode:**
  ```text
  saved = editor.snapshot()
  try: editor.apply(change)
  catch error: editor.restore(saved)
  ```
- **Source:** [Memento](https://refactoring.guru/design-patterns/memento)

### Observer

- **Intent:** Notify independent in-process subscribers when a subject changes or emits an event.
- **Pressure/participants:** Reactions vary independently and direct coupling is costly; subject owns subscription list, observers receive notifications.
- **Use/reject:** Use for explicit local notifications. Prefer direct calls for required synchronous business steps and a domain messaging skill for broker guarantees.
- **Trade-offs/proof:** Adds extensibility but raises unsubscribe, ordering, duplicate, exception, and backpressure questions. Test subscribe/unsubscribe/order/error behavior.
- **Pseudocode:**
  ```text
  class Subject {
    listeners = []
    subscribe(listener) { listeners.add(listener) }
    update(value) { for listener in listeners: listener(value) }
  }
  subject.subscribe(rebuild_index)
  subject.subscribe(refresh_view)
  subject.update(value)
  ```
- **Source:** [Observer](https://refactoring.guru/design-patterns/observer)

### State

- **Intent:** Represent state-specific behavior and transitions as replaceable state objects behind a context.
- **Pressure/participants:** Lifecycle states have growing invariants and different behavior; context delegates, state handles operation/transition, client drives context.
- **Use/reject:** Use when transitions and behavior are substantial. Prefer an enum plus transition function for a small finite state machine.
- **Trade-offs/proof:** Localizes lifecycle rules but adds objects and transition indirection. Test the transition table, invalid transitions, persistence, and state-dependent errors.
- **Pseudocode:**
  ```text
  class Order { state = Draft }
  Draft.submit(order) { receipt = charge(order); order.state = Paid(receipt) }
  Paid.cancel(order) { reject("already paid") }
  ```
- **Source:** [State](https://refactoring.guru/design-patterns/state)

### Strategy

- **Intent:** Encapsulate interchangeable algorithms behind one contract and choose one for a context.
- **Pressure/participants:** Algorithms vary independently or selection is runtime-configurable; context delegates to strategy, client selects it.
- **Use/reject:** Use for recurring algorithm variation or isolated algorithm tests. Prefer a callable, map, or `match` for a tiny closed choice.
- **Trade-offs/proof:** Makes algorithms replaceable but requires a clear contract and selection policy. Test the contract and representative cases for every strategy.
- **Pseudocode:**
  ```text
  interface Pricing { quote(cart) }
  checkout = Checkout(pricing=MemberPricing())
  total = checkout.total(cart)  // delegates quote calculation
  ```
- **Source:** [Strategy](https://refactoring.guru/design-patterns/strategy)

### Template Method

- **Intent:** Fix an algorithm’s invariant sequence while allowing controlled steps to vary in subclasses.
- **Pressure/participants:** Several implementations share ordering but differ at explicit hooks; base owns skeleton, subclasses implement hooks.
- **Use/reject:** Use when inheritance and invariant ordering are legitimate. Prefer composition/callables when extension points multiply or subtype substitution is weak.
- **Trade-offs/proof:** Enforces sequence but couples subclasses to base internals. Test sequence, hook count, exceptions, and each subclass contract.
- **Pseudocode:**
  ```text
  class ImportJob {
    run(input) { data = read(input); validate(data); persist(data) }
    validate(data) { /* hook */ }
  }
  class CsvImport extends ImportJob { validate(data) { check_columns(data) } }
  ```
- **Source:** [Template Method](https://refactoring.guru/design-patterns/template-method)

### Visitor

- **Intent:** Add operations over a stable set of element types without putting every operation into each element.
- **Pressure/participants:** Operations multiply while object structure changes rarely; elements dispatch to visitor, visitor implements type-specific operations.
- **Use/reject:** Use for a stable AST/object graph with many operations. Prefer methods, `match`, or `singledispatch` when structure or operations are small/changing together.
- **Trade-offs/proof:** Makes new operations local but couples visitors to every element type and makes new element types expensive. Test exhaustive dispatch and each operation.
- **Pseudocode:**
  ```text
  interface Node { accept(visitor) }
  Number.accept(v) { return v.number(this) }
  Add.accept(v) { return v.add(this) }
  PrintVisitor.add(node) { return "(" + node.left.accept(this) + " + " + node.right.accept(this) + ")" }
  ```
- **Source:** [Visitor](https://refactoring.guru/design-patterns/visitor)
