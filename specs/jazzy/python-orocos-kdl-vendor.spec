# Meta Package
Name:           ros-jazzy-python-orocos-kdl-vendor
Version:        0.5.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-python_orocos_kdl_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-python_orocos_kdl_vendor
Requires:       ros2-jazzy-python_orocos_kdl_vendor-devel

Obsoletes: ros-jazzy-python-orocos-kdl-vendor < 0.5.1-1

%description
Wrapper around PyKDL, providing nothing but a dependency on PyKDL on
some systems. On others, it fetches and builds python_orocos_kdl
locally.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.5.1-1
- Update to latest release
