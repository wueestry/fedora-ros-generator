# Meta Package
Name:           ros-jazzy-gz-transport-vendor
Version:        0.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://github.com/gazebosim/gz-transport
Summary:        Meta package for ros2-jazzy-gz_transport_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-gz_transport_vendor
Requires:       ros2-jazzy-gz_transport_vendor-devel

Obsoletes: ros-jazzy-gz-transport-vendor < 0.0.5-1

%description
Vendor package for: gz-transport13 13.4.0 Gazebo Transport: Provides
fast and efficient asynchronous message passing, services, and data
logging.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Jul 22 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.5-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.0.4-1
- Update to latest release
