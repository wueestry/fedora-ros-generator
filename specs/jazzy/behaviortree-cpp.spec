# Meta Package
Name:           ros-jazzy-behaviortree-cpp
Version:        4.6.1
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-behaviortree_cpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-behaviortree_cpp
Requires:       ros2-jazzy-behaviortree_cpp-devel

Obsoletes: ros-jazzy-behaviortree-cpp < 4.6.1-1

%description
This package provides the Behavior Trees core library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.6.1-1
- Update to latest release
