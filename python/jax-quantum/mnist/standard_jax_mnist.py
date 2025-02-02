import jax
import jax.numpy as jnp
import optax
import tensorflow_datasets as tfds
from jax import random
from jax import grad, jit, vmap
from jax.scipy.special import logsumexp

# Load the MNIST dataset
def load_mnist():
    ds_builder = tfds.builder('mnist')
    ds_builder.download_and_prepare()
    train_ds = tfds.as_numpy(ds_builder.as_dataset(split='train', batch_size=-1))
    test_ds = tfds.as_numpy(ds_builder.as_dataset(split='test', batch_size=-1))
    train_images, train_labels = train_ds['image'], train_ds['label']
    test_images, test_labels = test_ds['image'], test_ds['label']
    train_images = jnp.float32(train_images) / 255.0
    test_images = jnp.float32(test_images) / 255.0
    return train_images, train_labels, test_images, test_labels

train_images, train_labels, test_images, test_labels = load_mnist()

# Initialize parameters
def init_params(key):
    keys = random.split(key, 3)
    params = {
        'W1': random.normal(keys[0], (784, 128)) * 0.01,
        'b1': jnp.zeros(128),
        'W2': random.normal(keys[1], (128, 64)) * 0.01,
        'b2': jnp.zeros(64),
        'W3': random.normal(keys[2], (64, 10)) * 0.01,
        'b3': jnp.zeros(10),
    }
    return params

# Define the model
def forward(params, x):
    x = x.reshape(-1, 784)
    x = jax.nn.relu(jnp.dot(x, params['W1']) + params['b1'])
    x = jax.nn.relu(jnp.dot(x, params['W2']) + params['b2'])
    x = jnp.dot(x, params['W3']) + params['b3']
    return x

# Define the loss function
def cross_entropy_loss(params, x, y):
    logits = forward(params, x)
    one_hot = jax.nn.one_hot(y, num_classes=10)
    log_probs = logits - logsumexp(logits, axis=1, keepdims=True)
    return -jnp.mean(jnp.sum(one_hot * log_probs, axis=1))

# Define the accuracy function
def accuracy(params, x, y):
    logits = forward(params, x)
    predictions = jnp.argmax(logits, axis=1)
    return jnp.mean(predictions == y)

# Training step
@jit
def update(params, opt_state, x, y):
    loss, grads = jax.value_and_grad(cross_entropy_loss)(params, x, y)
    grads = jax.tree_map(lambda g: jnp.clip(g, -1.0, 1.0), grads)  # Gradient clipping
    updates, opt_state = optimizer.update(grads, opt_state)
    params = optax.apply_updates(params, updates)
    return params, opt_state, loss

# Initialize parameters and optimizer
key = random.PRNGKey(0)
params = init_params(key)
optimizer = optax.chain(
    optax.clip_by_global_norm(1.0),  # Gradient clipping
    optax.adam(learning_rate=0.0001)  # Reduced learning rate
)
opt_state = optimizer.init(params)

# Training loop
n_epochs = 20
batch_size = 128
num_batches = train_images.shape[0] // batch_size

for epoch in range(n_epochs):
    for i in range(num_batches):
        batch_start = i * batch_size
        batch_end = (i + 1) * batch_size
        x_batch = train_images[batch_start:batch_end]
        y_batch = train_labels[batch_start:batch_end]
        params, opt_state, loss = update(params, opt_state, x_batch, y_batch)
    
    train_acc = accuracy(params, train_images, train_labels)
    test_acc = accuracy(params, test_images, test_labels)
    print(f'Epoch {epoch + 1}, Loss: {loss:.4f}, Train Accuracy: {train_acc * 100:.2f}%, Test Accuracy: {test_acc * 100:.2f}%')

# Final evaluation
final_train_acc = accuracy(params, train_images, train_labels)
final_test_acc = accuracy(params, test_images, test_labels)
print(f'Final Train Accuracy: {final_train_acc * 100:.2f}%')
print(f'Final Test Accuracy: {final_test_acc * 100:.2f}%')