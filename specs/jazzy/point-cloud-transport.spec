# Meta Package
Name:           ros-jazzy-point-cloud-transport
Version:        4.0.4
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-point_cloud_transport and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-point_cloud_transport
Requires:       ros2-jazzy-point_cloud_transport-devel

Obsoletes: ros-jazzy-point-cloud-transport < 4.0.4-1

%description
Support for transporting PointCloud2 messages in compressed format and
plugin interface for implementing additional PointCloud2 transports.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.4-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.3-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.2-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.1-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.0-1
- Update to latest release
