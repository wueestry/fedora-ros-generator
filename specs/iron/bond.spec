# Meta Package
Name:           ros-iron-bond
Version:        4.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/bond
Summary:        Meta package for ros2-iron-bond and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-bond
Requires:       ros2-iron-bond-devel

Obsoletes: ros-iron-bond < 4.0.0-1

%description
A bond allows two processes, A and B, to know when the other has
terminated, either cleanly or by crashing. The bond remains connected
until it is either broken explicitly or until a heartbeat times out.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.0.0-1
- Update to latest release
