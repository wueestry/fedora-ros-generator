# Meta Package
Name:           ros-jazzy-urdfdom
Version:        4.0.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-urdfdom and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-urdfdom
Requires:       ros2-jazzy-urdfdom-devel

Obsoletes: ros-jazzy-urdfdom < 4.0.1-1

%description
A library to access URDFs using the DOM model.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.0-1
- Update to latest release
