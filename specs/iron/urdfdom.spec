# Meta Package
Name:           ros-iron-urdfdom
Version:        3.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-urdfdom and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-urdfdom
Requires:       ros2-iron-urdfdom-devel

Obsoletes: ros-iron-urdfdom < 3.1.1-1

%description
A library to access URDFs using the DOM model.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.3.1.1-1
- Update to latest release
