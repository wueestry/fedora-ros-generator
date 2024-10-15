# Meta Package
Name:           ros-jazzy-bond
Version:        4.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/bond
Summary:        Meta package for ros2-jazzy-bond and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-bond
Requires:       ros2-jazzy-bond-devel

Obsoletes: ros-jazzy-bond < 4.1.0-1

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
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.0-1
- Update to latest release
