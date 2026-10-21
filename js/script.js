/**
 * DevOps Portfolio & Practical Repository - Interactive Scripts
 * Author: Rutuja Deepak Jagtap (PCCOE Pune, PRN: 123B1B146)
 * Vanilla JavaScript (ES6+)
 */

document.addEventListener('DOMContentLoaded', () => {
  initThemeToggle();
  initMobileNavigation();
  initScrollSpy();
  initAssignmentFilters();
  initAssignmentModal();
  initContactForm();
});

/* --------------------------------------------------------------------------
   1. Dark / Light Theme Toggle System
   -------------------------------------------------------------------------- */
function initThemeToggle() {
  const themeToggleBtn = document.getElementById('themeToggle');
  const htmlElement = document.documentElement;
  
  // Check stored theme or match system preference
  const savedTheme = localStorage.getItem('portfolio-theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const initialTheme = savedTheme || (prefersDark ? 'dark' : 'light');

  setTheme(initialTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      setTheme(newTheme);
      localStorage.setItem('portfolio-theme', newTheme);
    });
  }

  function setTheme(theme) {
    htmlElement.setAttribute('data-theme', theme);
    if (themeToggleBtn) {
      themeToggleBtn.setAttribute('title', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
  }
}

/* --------------------------------------------------------------------------
   2. Mobile Hamburger Navigation
   -------------------------------------------------------------------------- */
function initMobileNavigation() {
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mainNav = document.getElementById('mainNav');
  const navLinks = document.querySelectorAll('.nav-link');

  if (mobileMenuBtn && mainNav) {
    mobileMenuBtn.addEventListener('click', () => {
      const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
      mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
      mainNav.classList.toggle('open');
    });

    // Close menu when a navigation link is clicked
    navLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mainNav.classList.remove('open');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!mainNav.contains(e.target) && !mobileMenuBtn.contains(e.target) && mainNav.classList.contains('open')) {
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mainNav.classList.remove('open');
      }
    });
  }
}

/* --------------------------------------------------------------------------
   3. Active Section Scroll Spy
   -------------------------------------------------------------------------- */
function initScrollSpy() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  if (!sections.length || !navLinks.length) return;

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('href') === `#${id}`) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => observer.observe(section));
}

/* --------------------------------------------------------------------------
   4. DevOps Assignment Filtering
   -------------------------------------------------------------------------- */
function initAssignmentFilters() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.assignment-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Update active button state
      filterBtns.forEach(b => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const filterValue = btn.getAttribute('data-filter');

      cards.forEach(card => {
        const categories = card.getAttribute('data-category') || '';
        if (filterValue === 'all' || categories.split(' ').includes(filterValue)) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 10);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 200);
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   5. Assignment Quick View Modal System
   -------------------------------------------------------------------------- */
const assignmentData = {
  'modal-asg-6': {
    title: 'Assignment 06: Jenkins & GitHub Continuous Integration',
    category: 'CI/CD & Automation',
    aim: 'To configure Jenkins with a GitHub repository and automate the process of pulling source code from the repository for Continuous Integration.',
    problem: 'Manual code pulling and unsynchronized testing create integration bottlenecks. The objective is to automate code checkout and execute testing upon every commit.',
    technologies: ['Jenkins Automation Server', 'Git & GitHub SCM', 'Python Flask REST API', 'Unittest Suite', 'Jenkins Declarative Pipeline'],
    commands: [
      'git checkout -b feature-update',
      'python -m unittest test_app.py',
      'python -m py_compile app.py',
      'curl -X POST http://jenkins.local:8080/github-webhook/'
    ],
    folder: 'assignments/assignment-06-jenkins-github/',
    manual: 'assignments/assignment-06-jenkins-github/README.md',
    pdf: 'assets/docs/123B1B146_RUTUJA_JAGTAP_DevOps_Assignment_6_Jenkins_GitHub.pdf'
  },
  'modal-asg-7': {
    title: 'Assignment 07: Kubernetes & Helm Container Orchestration',
    category: 'Kubernetes & Helm',
    aim: 'To study Kubernetes architecture and understand the structure and commands of Helm for managing containerized applications.',
    problem: 'Managing complex workloads via raw YAML manifests leads to configuration drift. Helm packages multi-resource applications into reusable, versioned charts.',
    technologies: ['Kubernetes Control Plane', 'Worker Nodes', 'Helm v3 Package Manager', 'Go-Template Syntax', 'Nginx Pod Workload'],
    commands: [
      'helm create myapp',
      'helm template myapp ./myapp',
      'helm install my-release ./myapp',
      'helm upgrade my-release ./myapp --set replicaCount=3',
      'helm list -A'
    ],
    folder: 'assignments/assignment-07-kubernetes-helm/',
    manual: 'assignments/assignment-07-kubernetes-helm/README.md',
    pdf: 'assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_7_Kubernetes_Helm.pdf'
  },
  'modal-asg-8': {
    title: 'Assignment 08: Kubernetes Objects & Ansible Configuration Management',
    category: 'Kubernetes & Ansible',
    aim: 'To study important Kubernetes objects and networking services and demonstrate the use of Ansible for automated configuration management.',
    problem: 'Managing microservices requires deep understanding of K8s objects (Pods, Deployments, Services), while configuring physical/virtual nodes demands agentless automation.',
    technologies: ['Kubernetes Pods & Deployments', 'NodePort Service', 'Ansible Control Node', 'OpenSSH Transport', 'Idempotent Playbooks'],
    commands: [
      'kubectl apply -f pod.yaml',
      'kubectl apply -f deployment.yaml',
      'kubectl expose deployment nginx-deployment --type=NodePort --port=80',
      'ansible webservers -i inventory.ini -m ping',
      'ansible-playbook -i inventory.ini install-nginx.yml'
    ],
    folder: 'assignments/assignment-08-k8s-ansible/',
    manual: 'assignments/assignment-08-k8s-ansible/README.md',
    pdf: 'assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_8_K8s_Ansible.pdf'
  },
  'modal-asg-9': {
    title: 'Assignment 09: Container Orchestration & Helm Chart Management',
    category: 'Kubernetes & Helm',
    aim: 'To explore container orchestration in Kubernetes, analyze control-plane/worker topology, and examine Helm chart anatomy and lifecycle commands.',
    problem: 'Analyzing distributed control plane reconciliation and packaging microservice manifests into modular Helm chart structures with release lifecycle operations.',
    technologies: ['kube-apiserver & etcd', 'kube-scheduler & kube-controller-manager', 'kubelet & kube-proxy', 'Chart.yaml & values.yaml', 'Helm Rollback'],
    commands: [
      'helm lint ./webapp-chart',
      'helm install webapp-release ./webapp-chart',
      'helm status webapp-release',
      'helm history webapp-release',
      'helm rollback webapp-release 1'
    ],
    folder: 'assignments/assignment-09-kubernetes-helm/',
    manual: 'assignments/assignment-09-kubernetes-helm/README.md',
    pdf: 'assets/docs/123B1B146_RUTUJA_JAGTAP_DevOps_Assignment_9_Kubernetes_Helm.pdf'
  },
  'modal-asg-10': {
    title: 'Assignment 10: Kubernetes Objects & Service Networking Architecture',
    category: 'Kubernetes Networking',
    aim: 'To explore core Kubernetes objects (Pods, Deployments, Namespaces, ConfigMaps, Secrets, PV/PVC) and evaluate the 4 service routing types.',
    problem: 'Microservice applications require robust decoupled configuration, encrypted credentials, persistent storage, and specialized networking across service types.',
    technologies: ['ClusterIP Service', 'NodePort Service', 'LoadBalancer Service', 'ExternalName Service', 'PersistentVolumeClaim (PVC)'],
    commands: [
      'kubectl apply -f 01-namespace.yaml',
      'kubectl apply -f 02-configmap-secret.yaml',
      'kubectl apply -f 03-pv-pvc.yaml',
      'kubectl apply -f 04-deployment.yaml',
      'kubectl apply -f 05-services.yaml',
      'kubectl get svc -n dev-space -o wide'
    ],
    folder: 'assignments/assignment-10-k8s-objects-services/',
    manual: 'assignments/assignment-10-k8s-objects-services/README.md',
    pdf: 'assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_10_K8s_Objects_Services.pdf'
  },
  'modal-asg-11': {
    title: 'Assignment 11: Ansible Configuration Management & Enterprise Stack',
    category: 'Ansible & IaC',
    aim: 'To evaluate Ansible agentless configuration management and demonstrate automated provisioning of an enterprise multi-tier web application stack.',
    problem: 'Manual multi-server provisioning leads to configuration drift, human error, and slow deployment. Ansible automates complete multi-tier stacks idempotently.',
    technologies: ['Ansible Control Node', 'Jinja2 Upstream Templating', 'Nginx Load Balancer', 'PostgreSQL Hardened DB', 'Modular Ansible Roles'],
    commands: [
      'ansible-inventory -i inventory.ini --graph',
      'ansible all -i inventory.ini -m ping',
      'ansible-playbook -i inventory.ini site.yml --syntax-check',
      'ansible-playbook -i inventory.ini site.yml',
      'curl -I http://192.168.1.50'
    ],
    folder: 'assignments/assignment-11-ansible-case-study/',
    manual: 'assignments/assignment-11-ansible-case-study/README.md',
    pdf: 'assets/docs/123B1B146_Rutuja_Jagtap_DevOps_Assignment_11_Ansible_Case_Study.pdf'
  }
};

function initAssignmentModal() {
  const modal = document.getElementById('assignmentModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalTitle = document.getElementById('modalTitle');
  const modalBody = document.getElementById('modalBody');
  const modalManualLink = document.getElementById('modalManualLink');
  const modalPdfLink = document.getElementById('modalPdfLink');
  const viewButtons = document.querySelectorAll('.view-details-btn');

  if (!modal) return;

  viewButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const modalKey = btn.getAttribute('data-modal');
      const data = assignmentData[modalKey];

      if (data) {
        modalTitle.textContent = data.title;
        modalBody.innerHTML = `
          <div style="margin-bottom: 1rem;">
            <span class="asg-badge badge-cicd" style="font-size: 0.75rem;">${data.category}</span>
          </div>
          <h4>Aim</h4>
          <p>${data.aim}</p>
          <h4>Problem Statement</h4>
          <p>${data.problem}</p>
          <h4>Core Technologies</h4>
          <p>${data.technologies.map(t => `<span class="hl-tag" style="display:inline-block; margin: 2px;">${t}</span>`).join('')}</p>
          <h4>Key Verification Commands</h4>
          <ul>
            ${data.commands.map(c => `<li><code>${c}</code></li>`).join('')}
          </ul>
        `;

        modalManualLink.setAttribute('href', data.manual);
        modalPdfLink.setAttribute('href', data.pdf);

        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  const closeModal = () => {
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  };

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
      closeModal();
    }
  });
}

/* --------------------------------------------------------------------------
   6. Contact Form Validation & Submission Feedback
   -------------------------------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById('contactForm');
  const feedback = document.getElementById('formFeedback');

  if (!form || !feedback) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    let isValid = true;

    const nameInput = document.getElementById('contactName');
    const emailInput = document.getElementById('contactEmail');
    const subjectInput = document.getElementById('contactSubject');
    const messageInput = document.getElementById('contactMessage');

    const nameError = document.getElementById('nameError');
    const emailError = document.getElementById('emailError');
    const subjectError = document.getElementById('subjectError');
    const messageError = document.getElementById('messageError');

    // Name check
    if (!nameInput.value.trim()) {
      nameError.classList.add('visible');
      isValid = false;
    } else {
      nameError.classList.remove('visible');
    }

    // Email check
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailInput.value.trim())) {
      emailError.classList.add('visible');
      isValid = false;
    } else {
      emailError.classList.remove('visible');
    }

    // Subject check
    if (!subjectInput.value.trim()) {
      subjectError.classList.add('visible');
      isValid = false;
    } else {
      subjectError.classList.remove('visible');
    }

    // Message check
    if (!messageInput.value.trim()) {
      messageError.classList.add('visible');
      isValid = false;
    } else {
      messageError.classList.remove('visible');
    }

    if (isValid) {
      feedback.className = 'form-feedback success';
      feedback.innerHTML = `<strong>Thank you, ${escapeHtml(nameInput.value.trim())}!</strong> Your message has been prepared. For direct communication, you can also reach me at <a href="mailto:rutuja.jagtap23@pccoepune.org" style="text-decoration:underline;">rutuja.jagtap23@pccoepune.org</a>.`;
      form.reset();
    }
  });

  function escapeHtml(str) {
    return str.replace(/[&<>'"]/g, tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag));
  }
}
